#!/usr/bin/env python2.7
import logging
import json
try:
    from bs4 import BeautifulSoup, SoupStrainer
except ImportError:
    print('Missing BeautifulSoup try: "pip install beautifulsoup4"')
    quit(1)
import requests
import subprocess
import os

FORMAT = '%(asctime)-15s %(levelname)s %(module)s.%(funcName)s %(message)s'
DATEFMT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATEFMT)

    # def update_role(self, **kwargs):
    #     """Updates information for a role.

    #     http://documentation.agilepoint.com/SupportPortal/DOCS/ProductDocumentation/CurrentRelease/DocumentationLibrary/maps/restmethodUpdateRole.html

    #     Path Args: None
    #     Required Body Args: Description, Enabled, Rights, RoleName
    #     Optional Body Args: None"""
    #     req_args = ['Description', 'Enabled', 'Rights', 'RoleName']
    #     validate_args(kwargs, req_args)
    #     resp = self.admin.UpdateRole.POST(data=json.dumps(kwargs))
    #     return handle_response('json', resp)

BASE_PATH = 'documentation.agilepoint.com/SupportPortal/DOCS/ProductDocumentation'
BASE_PATH += '/CurrentRelease/DocumentationLibrary/maps'

def munge_element(ele):
    # new_ele = []
    # for sec in ele:
    if '\n' in ele:
        print(type(ele))
        print('found newline')
        cols = [e.strip() for e in ele.split('\n')]
        return dict(zip(cols[0::2], cols[1::2]))
    else:
        return ele

def fix_camel_case(string):
    newstring = ''
    first = True
    for char in string:
        if char.isupper():
            if first:
                first = False
            else:
                newstring += '_'
        newstring += char.lower()
        newstring = newstring.replace('e_mail', 'email')
        newstring = newstring.replace('u_u_i_d', 'uuid')
        newstring = newstring.replace('_i_d', '_id')
    return newstring

def describe_class(class_name):
    req_args = []
    file_name = '{}/restapiclass{}.html'.format(BASE_PATH, class_name)
    if os.path.exists(file_name):
        f_handle = open(file_name, 'r')
        soup = BeautifulSoup(f_handle.read(), 'html.parser')
        try:
            table = soup.find('div', id='Properties').table
            tr_ = table.find_all('tr', class_='strow', recursive=False)
            for row in tr_:
                td_ = row.find('td', class_='stentry', recursive=False)
                req_args.append(td_.text.strip())
        except AttributeError as error:
            logging.error('Unable to finish processing describe_class for %s', file_name)
            raise
    else:
        logging.error('Unable to finish processing describe_class for %s', file_name)
    return req_args

class PyMethod(object):
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.req_args = []
        self.path_args = []
        self.methodname = ''
        self.restapi = ''
        self.section = ''
        self.description = ''
        self.resp_type = ''
        self.req_type = ''

    def parse_html(self):
        # print('Generating method')

        for tag in self.soup.find_all('div', class_='section'):
            if tag.find('h2').text == 'URL Format (On Premises)':
                restmethod = tag.p
                restmethod.span.span.extract()
                self.section = restmethod.span.text.strip('/')
                restmethod.span.extract()
                self.restapi = restmethod.text.split('/')[0].strip()
                self.methodname = fix_camel_case(self.restapi)

            elif tag.find('h2').text == 'HTTP Method':
                self.req_type = tag.p.text.strip()

            elif tag.find('h2').text == 'Request Parameters':
                self.path_args = []
                for row in tag.table.find_all('tr'):
                    path_arg = row.find('td')
                    if path_arg:
                        path_arg = path_arg.text.strip()
                        if path_arg != 'None':
                            self.path_args.append(path_arg)

            elif tag.find('h2').text == 'Request Body Properties':
                self.req_args = []
                data = []
                for i, row in enumerate(tag.table.find_all('tr', class_='strow')):
                    # logging.info('Table row %s', i)
                    property_ = row.find('td', class_='stentry').text.strip()
                    if property_ in ['instruction', 'expr']:
                        logging.warning('Found non arg in arg list for %s', self.restapi)
                        index = 0
                        for i_, dt_ in enumerate(row.find_all('dt', class_='dt dlterm')):
                            # logging.info('DT row %s', i_)
                            if dt_.text == 'Type':
                                index = i_
                        for i_, dd_ in enumerate(row.find_all('dd', class_='dd')):
                            # logging.info('DD row %s', i_)
                            if index == i_:
                                self.req_args.extend(describe_class(dd_.text.strip()))
                    else:
                        self.req_args.append(property_)

            elif tag.find('h2').text == 'JSON Response Body Example':
                if tag.pre:
                    if tag.pre.text.startswith('{'):
                        self.resp_type = 'json'
                    else:
                        self.resp_type = 'text'
                else:
                    self.resp_type = 'bool'
            elif tag.find('h2').text == 'Description':
                self.description = ' '.join(tag.p.text.split('\n')).encode('utf-8')
            else:
                # print(tag.find('h2').text)
                pass

        self.url = 'http://{}/restmethod{}.html'.format(BASE_PATH, self.restapi)

    def generate_method(self):
        method = []

        line1 = '    def {methodname}(self'.format(methodname=self.methodname)
        if len(self.path_args) > 0:
            line1 += ', {}'.format(', '.join([fix_camel_case(a) for a in self.path_args]))
        if len(self.req_args) > 0:
            line1 += ', **kwargs'
        line1 += '):'
        method.append(line1)

        line2 = '        """{description}'.format(description=self.description)
        method.append(line2)
        method.append('')
        method.append('        {}'.format(self.url))
        method.append('')

        if len(self.path_args) > 0:
            method.append('        Path Args: {}'.format(', '.join(self.path_args)))
        else:
            method.append('        Path Args: None')

        if len(self.req_args) > 0:
            method.append('        Required Body Args: {}'.format(', '.join(self.req_args)))
            # method.append('    Optional Body Args: {}"""'.format(', '.join(self.req_args)))
            method.append('        Optional Body Args: None"""')
            method.append('        req_args = {}'.format(repr(self.req_args)))
            method.append('        validate_args(kwargs, req_args)')
        else:
            method.append('        Required Body Args: None')
            method.append('        Optional Body Args: None"""')

        line8 = '        resp = self.{}.{}'.format(self.section.lower(), self.restapi)
        if len(self.path_args) > 0:
            for arg in [fix_camel_case(a) for a in self.path_args]:
                line8 += '({})'.format(arg)

        line8 += '.{}'.format(self.req_type.upper())
        if len(self.req_args) > 0:
            line8 += '(data=json.dumps(kwargs))'
        else:
            line8 += '()'
        method.append(line8)

        method.append("        return handle_response('{}', resp)".format(self.resp_type))
        return '\n'.join(method)
        
    def __repr__(self):
        return '<PyMethod: section={section} || restapi={restapi} || methodname={methodname} || url={url} || resp_type={resp_type} || req_args={req_args} || path_args={path_args} || description={description}>'.format(
            section=self.section,
            restapi=self.restapi,
            methodname=self.methodname,
            url=self.url,
            resp_type=self.resp_type,
            req_args=', '.join(self.req_args),
            path_args=', '.join(self.path_args),
            req_type=self.req_type,
            description=self.description)


FNULL = open(os.devnull, 'w')

def write_header(section):
    resp = []
    resp.append('"""{} Methods for AgilePoint API"""'.format(section))
    resp.append('import json')
    resp.append('from ._utils import handle_response, validate_args')
    resp.append('# pylint: disable=too-many-public-methods,too-many-lines')
    resp.append('')
    resp.append('')
    resp.append('class {}(object):'.format(section))
    resp.append('    """{} Methods for AgilePoint API"""'.format(section))
    resp.append('    def __init__(self, agilepoint):')
    resp.append('        self.{} = agilepoint.agilepoint.{}'.format(section.lower(), section))
    resp.append('        self.agilepoint = agilepoint')
    resp.append('')
    return '\n'.join(resp)


def main():
    stor_dir = 'api_docs'

    if os.path.exists(stor_dir):
        os.chdir(stor_dir)
        print('Skipping mirror process. Mirror exists.')
        print('If you need to refresh remove the dir {}'.format(stor_dir))
    else:
        print('Mirroring of the current doc site. This will take a while')
        os.mkdir(stor_dir)
        os.chdir(stor_dir)
        mirror_url = 'http://{}/index.html'.format(BASE_PATH)
        subprocess.call(['wget', '--mirror', '--quiet', '--accept', 'htm,html',
                         mirror_url], stdout=FNULL, stderr=subprocess.STDOUT)
        print('Completed mirror process')

    count = 0
    admin_write = open('admin.py', 'w')
    workflow_write = open('workflow.py', 'w')

    admin_write.write(write_header('Admin'))
    admin_write.write('\n')

    workflow_write.write(write_header('Workflow'))
    workflow_write.write('\n')
    
    file_names = []
    for subdir, dirs, files in os.walk(BASE_PATH):
        for filename in files:
            if 'restmethod' not in filename:
                continue
            # Skipping this becuase it's not a method so much as it is documentation for how to auth
            if 'restmethodAuthentication' in filename:
                continue
            full_path = os.path.join(subdir, filename)
            file_names.append(full_path)

    for full_path in sorted(file_names):
        # print(full_path)
        f_handle = open(full_path)
        method = PyMethod(f_handle.read())
        f_handle.close()
        method.parse_html()
        if method.section == 'Workflow':
            workflow_write.write(method.generate_method())
            workflow_write.write('\n\n')
        elif method.section == 'Admin':
            admin_write.write(method.generate_method())
            admin_write.write('\n\n')
        else:
            logging.error('Unable to find useable section for %s', full_path)
            logging.error(repr(method))
        # print(repr(method))
        # quit()

if __name__ == '__main__':
    main()
