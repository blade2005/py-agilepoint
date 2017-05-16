"""Admin Methods for AgilePoint API"""
import json
import requests
from .exceptions import MissingRequiredArg, InvalidArg
# pylint: disable=no-member,too-many-public-methods


class Admin(object):
    """Admin Methods for AgilePoint API"""
    def __init__(self, agilepoint):
        self.admin = agilepoint.Admin

    def activate_delegation(self, delegationid):
        """Activates a delegation.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.ActivateDelegation(delegationid).POST()
        return resp.status_code == requests.codes.ok

    def add_delegation(self, **kwargs):
        """Creates a rule for delegating one user's tasks to another user.

        Path Args: None
        Required Body Args: FromUser, ToUser, StartDate, EndDate, Description
        Optional Body Args: None"""
        req_args = ['FromUser', 'ToUser', 'StartDate', 'EndDate', 'Description']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddDelegation.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def add_e_mail_template(self, **kwargs):
        """Adds an email template to the AgilePoint system.

        Path Args: None
        Required Body Args: TemplateOwnerID, MailTemplateXML
        Optional Body Args: None"""
        req_args = ['TemplateOwnerID', 'MailTemplateXML']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddEMailTemplate.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.text

    def add_group(self, **kwargs):
        """Adds a group to the AgilePoint system.

        Path Args: None
        Required Body Args: GroupName, ResponsibleUser
        Optional Body Args: Enabled, Description"""
        req_args = ['GroupName', 'ResponsibleUser']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddGroup.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def add_group_member(self, **kwargs):
        """Adds a user as a member of a group.

        Path Args: None
        Required Body Args: Description, Enabled, GroupName, UserName
        Optional Body Args: ClientData"""
        req_args = ['Description', 'Enabled', 'GroupName', 'UserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddGroupMember.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def add_role(self, **kwargs):
        """Adds a role to the AgilePoint system.

        Path Args: None
        Required Body Args: RoleName, Description, Rights, Enabled
        Optional Body Args: None"""
        req_args = ['RoleName', 'Description', 'Rights', 'Enabled']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddRole.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def add_role_member(self, **kwargs):
        """Adds a user or a group to a role.

        Path Args: None
        Required Body Args: Assignee, AssigneeType, ClientData, ObjectID,
                            ObjectType, RoleName
        Optional Body Args: None"""
        req_args = ['Assignee', 'AssigneeType', 'ClientData', 'ObjectID',
                    'ObjectType', 'RoleName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.AddRoleMember.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def cancel_delegation(self, delegationid):
        """Cancels a currently operating delegation.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.CancelDelegation(delegationid).POST()
        return resp.status_code == requests.codes.ok

    def get_access_right_names(self):
        """Retrieves the names of all the access rights in the AgilePoint system.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetAccessRightNames.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_access_rights(self, **kwargs):
        """Retrieves the access rights for a specified user.

        Path Args: None
        Required Body Args: userName
        Optional Body Args: None"""
        req_args = ['userName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.GetAccessRights.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_all_e_mail_templates(self):
        """Retrieves all the global email templates from the server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetAllEMailTemplates.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_database_info(self):
        """Retrieves the database information of the current server configuration.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetDatabaseInfo.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_delegation(self, delegationid):
        """Retrieves a delegation object.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetDelegation(delegationid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_delegations(self, delegationid, **kwargs):
        """Retrieves a list of delegation objects that match the specified parameters.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: FromUser, ToUser, Status"""
        opt_args = ['FromUser', 'ToUser', 'Status']
        present_args = kwargs.keys()
        for arg in present_args:
            if arg not in opt_args:
                raise InvalidArg(arg)
        resp = self.admin.GetDelegations(delegationid).POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_domain_group_members(self, **kwargs):
        """Retrieves the members of a domain group.

        Path Args: None
        Required Body Args: groupDistinguishedName
        Optional Body Args: None"""
        req_args = ['groupDistinguishedName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.GetDomainGroupMembers.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_domain_groups(self, **kwargs):
        """Retrieves all the domain group objects.

        Path Args: None
        Required Body Args: Filter, LDAPPath
        Optional Body Args: None"""
        req_args = ['Filter', 'LDAPPath']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.GetDomainGroups.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_domain_name(self):
        """Retrieves the domain name to which AgilePoint Server connects.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetDomainName.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_domain_users(self, **kwargs):
        """Retrieves all the user information in the domain that AgilePoint
        Server connects. It could be a local Windows system user, or a domain
        controller on the network.

        Path Args: None
        Required Body Args: Filter, LDAPPath
        Optional Body Args: None"""
        req_args = ['Filter', 'LDAPPath']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.GetDomainUsers.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_e_mail_template(self, mailtemplateid):
        """Retrieves an email templates with the specified template name from
        the server.

        Path Args: mailTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetEMailTemplate(mailtemplateid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_group(self, groupname):
        """Retrieves a group object with the specified group name.

        Path Args: groupName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetGroup(groupname).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_group_members(self, groupname):
        """Retrieves the members of a specified group.

        Path Args: groupName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetGroupMembers(groupname).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_groups(self):
        """Retrieves all the group objects in the system.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetGroups.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_locale(self):
        """Retrieves the default locale for the AgilePoint Server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetLocale.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_register_user(self, **kwargs):
        """Retrieves the user information for the registered user.

        Path Args: None
        Required Body Args: userName
        Optional Body Args: None"""
        req_args = ['userName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.GetRegisterUser.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_register_users(self):
        """Retrieves all registered users.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetRegisterUsers.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_role(self, rolename):
        """Retrieves a role object by name.

        Path Args: roleName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetRole(rolename).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_roles(self):
        """Retrieves a list of all roles in the system.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetRoles.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_sender_e_mail_address(self):
        """Retrieves the sender email address of the AgilePoint Server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetSenderEMailAddress.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_smtp_server(self):
        """Retrieves the SMTP server of the current server configuration.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetSmtpServer.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_sys_perf_info(self):
        """Retrieves system performance information for AgilePoint Server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetSysPerfInfo.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_system_user(self):
        """Retrieves the name of the system user.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.GetSystemUser.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_register_users_using_sql(self, **kwargs):
        """Query the list of registered users in AgilePoint.

        Path Args: None
        Required Body Args: sqlWhereClause
        Optional Body Args: None"""
        req_args = ['sqlWhereClause']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.QueryRegisterUsersUsingSQL.POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_role_members(self, rolename):
        """Retrieves the members assigned to a role that match a specified SQL
        statement.

        Path Args: roleName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.QueryRoleMembers(rolename).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def register_user(self, **kwargs):
        """Registers a user on the AgilePoint system.

        Path Args: None
        Required Body Args: UserName
        Optional Body Args: Department, EMailAddress, FullName, Locale, Manager,
                            OnlineContact, RefID, RegisteredDate, TimeZone,
                            Title, UALExpirationDate, UALNeverExpires"""
        req_args = ['UserName']
        opt_args = ['Department', 'EMailAddress', 'FullName', 'Locale',
                    'Manager', 'OnlineContact', 'RefID', 'RegisteredDate',
                    'TimeZone', 'Title', 'UALExpirationDate', 'UALNeverExpires',
                    'UserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        for arg in present_args:
            if arg not in opt_args:
                raise InvalidArg(arg)
        resp = self.admin.RegisterUser.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def remove_delegation(self, delegationid):
        """Removes a delegation from the AgilePoint system.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.RemoveDelegation(delegationid).POST()
        return resp.status_code == requests.codes.ok

    def remove_group(self, groupname):
        """Removes a group from the AgilePoint system.

        Path Args: delegationID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.RemoveGroup(groupname).POST()
        return resp.status_code == requests.codes.ok

    def remove_group_member(self, **kwargs):
        """Removes a member from a group.

        Path Args: None
        Required Body Args: GroupName, UserName
        Optional Body Args: None"""
        req_args = ['GroupName', 'UserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.RemoveGroupMember.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def remove_role_member(self, **kwargs):
        """Removes a user or a group from a specified role.

        Path Args: None
        Required Body Args: Assignee, AssigneeType, ObjectID, RoleName
        Optional Body Args: None"""
        req_args = ['Assignee', 'AssigneeType', 'ObjectID', 'RoleName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.RemoveRoleMember.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def remove_role(self, rolename):
        """Removes a role from the AgilePoint system.

        Path Args: roleName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.admin.RemoveRole(rolename).POST()
        return resp.status_code == requests.codes.ok

    def unregister_user(self, **kwargs):
        """Removes a user's registration from the AgilePoint system. Note that
        this call does not remove the user from the local Windows system or the
        domain controller.

        Path Args: None
        Required Body Args: userName
        Optional Body Args: None"""
        req_args = ['userName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.UnregisterUser.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def update_delegation(self, **kwargs):
        """Updates a delegation object that has already been created.

        Path Args: None
        Required Body Args: DelegationID
        Optional Body Args: DelegationID, FromUser, ToUser, StartDate, EndDate,
                            Description, Status"""
        req_args = ['DelegationID', 'FromUser', 'ToUser', 'StartDate',
                    'EndDate', 'Description', 'Status']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.UpdateDelegation.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def update_e_mail_template(self, **kwargs):
        """Updates an email template in the AgilePoint database.

        Path Args: None
        Required Body Args: MailTemplateID, MailTemplateXML,
                            TemplateModifiedUserName
        Optional Body Args: None"""
        req_args = ['MailTemplateID', 'MailTemplateXML',
                    'TemplateModifiedUserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.UpdateEMailTemplate.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def update_group(self, **kwargs):
        """Updates information for a group.

        Path Args: None
        Required Body Args: Description, Enabled, GroupName, ResponsibleUser
        Optional Body Args: None"""
        req_args = ['Description', 'Enabled', 'GroupName', 'ResponsibleUser']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.UpdateGroup.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def update_register_user(self, **kwargs):
        """Updates user data for a registered user.

        Path Args: None
        Required Body Args: UserName
        Optional Body Args: Department, EMailAddress, FullName, Locale, Manager,
                            OnlineContact, RefID, TimeZone, Title"""
        req_args = ['UserName']
        opt_args = ['Department', 'EMailAddress', 'FullName', 'Locale',
                    'Manager', 'OnlineContact', 'RefID', 'TimeZone', 'Title',
                    'UserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        for arg in present_args:
            if arg not in opt_args:
                raise InvalidArg(arg)
        resp = self.admin.UpdateRegisterUser.POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def update_role(self, **kwargs):
        """Updates information for a role.

        Path Args: None
        Required Body Args: Description, Enabled, Rights, RoleName
        Optional Body Args: None"""
        req_args = ['Description', 'Enabled', 'Rights', 'RoleName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.admin.UpdateRole.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()
