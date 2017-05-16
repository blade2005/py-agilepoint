"""Workflow Methods for AgilePoint API"""
import json
import requests
from .exceptions import MissingRequiredArg, InvalidArg  # pylint: disable=unused-import
# pylint: disable=no-member,too-many-public-methods,too-many-lines


class Workflow(object):
    """Workflow Methods for AgilePoint API"""
    def __init__(self, agilepoint):
        self.workflow = agilepoint.Workflow

    def activate_work_item(self, workitemid, activate, **kwargs):
        """Activates a work item.

        Path Args: workItemID, activate
        Required Body Args: clientData
        Optional Body Args: None"""
        req_args = ['clientData']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.ActivateWorkItem(workitemid)(
            activate).POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def archive_proc_inst(self, procinstid):
        """Archives a process instance based on a specified process instance
        identifier by moving the set of process instance records from the
        current AgilePoint Database into the AgilePoint Archive Database.
        The process instance records and all of the associated data are then
        deleted from the AgilePoint Database. The process instance to be
        archived must be completed or canceled.

        Path Args: procInstID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.ArchiveProcInst(procinstid).POST()
        return resp.status_code == requests.codes.ok

    def assign_work_item(self, workitemid, **kwargs):
        """Assigns a work item to a user, which often means claiming a work
        item for oneself. This is often used with task pools where work items
        are created, and then multiple users are notified, but the work item
        is not immediately assigned to a user. A user then claims the work item,
        or his manager assigns it to him. The user must have privileges to
        claim or assign the work item.

        Path Args: workItemID
        Required Body Args: clientData
        Optional Body Args: None"""
        req_args = ['clientData']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.AssignWorkItem(workitemid).POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def cancel_activity_inst(self, activityinstanceid):
        """Cancels a manual activity instance along with all manual work items
        associated with the specified manual activity instance ID. Note that an
        activity instance can be associated with one or more manual work items.
        Once the manual activity instance is canceled, the process instance will
        move forward to the next activity.

        Path Args: activityInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CancelActivityInst(activityinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def cancel_mail_deliverable(self, mailid):
        """Cancels the failed mail deliverable record based on a given message
        identifier. Note that canceling the failed mail deliverable record
        prevents it from being recycled or present on a given interval by the
        AgilePoint engine.

        Path Args: mailID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CancelMailDeliverable(mailid).POST()
        return resp.status_code == requests.codes.ok

    def cancel_procedure(self, workitemid):
        """Cancels an automatic work item based on supplied specified automatic
        work item identifier.

        Path Args: workItemID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CancelProcedure(workitemid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def cancel_proc_inst(self, processinstanceid):
        """Cancels the process instance based on a specified process instance
        identifier. This method cancels all automatic work items, manual work
        items, and child process instances.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CancelProcInst(processinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def cancel_work_item(self, workitemid, **kwargs):
        """Cancels a manual work item based on a specified manual work item
        identifier. Only the following manual work item status can transition
        to a Canceled status: Assigned, New, Pseudo, and Overdue.

        Path Args: workItemID
        Required Body Args: clientData
        Optional Body Args: None"""
        req_args = ['clientData']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CancelWorkItem(
            workitemid).POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def checkin_proc_def(self, **kwargs):
        """Checks in the process definition to the AgilePoint Server and returns
        the process definition identifier. This method accepts a string with the
        updated process definition in XML format.

        Path Args: None
        Required Body Args: xml
        Optional Body Args: None"""
        req_args = ['xml']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CheckinProcDef.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def checkout_proc_def(self, processtemplateid):
        """This method is used to manage process definition versioning by
        setting the process definition status to CheckedOut based on a given
        process definition ID. Only process definitions with the status of
        Released can transition into the CheckedOut status.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CheckoutProcDef(processtemplateid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.text

    def complete_procedure(self, workitemid):
        """Marks an automatic work item as completed by an asynchronous
        activity.

        Path Args: workItemID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.CompleteProcedure(workitemid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def complete_work_item(self, workitemid, **kwargs):
        """Marks a work item as completed.

        Path Args: None
        Required Body Args: clientData
        Optional Body Args: None"""
        req_args = ['clientData']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CompleteWorkItem(workitemid).POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def create_linked_work_item(self, **kwargs):
        """Creates a manual work item that is linked to another manual work
        item. The work item you create does not depend on the completion of
        the work item to which it is linked. In other words, the original
        (source) work item can be marked as completed before new work item is
        completed.

        Path Args: None
        Required Body Args: bDependent, BusinessTime, ClientData, Length,
                            SourceWorkItemID, Unit, UserID, WorkToPerform
        Optional Body Args: None"""
        req_args = ['bDependent', 'BusinessTime', 'ClientData', 'Length',
                    'SourceWorkItemID', 'Unit', 'UserID', 'WorkToPerform']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CreateLinkedWorkItem.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def create_proc_def(self, **kwargs):
        """Adds a new process definition to the AgilePoint Server.

        Path Args: None
        Required Body Args: xml
        Optional Body Args: None"""
        resp = self.workflow.CreateProcDef.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def create_proc_inst(self, **kwargs):
        """Creates a process instance for a specified process definition ID and
        parameters.

        Path Args: None
        Required Body Args: Attributes, blnStartImmediately, CustomID,
                            Initiator, ProcessID, ProcessInstID, ProcInstName,
                            SuperProcInstID, WorkObjID, WorkObjInfo
        Optional Body Args: None"""
        req_args = ['Attributes', 'blnStartImmediately', 'CustomID',
                    'Initiator', 'ProcessID', 'ProcessInstID', 'ProcInstName',
                    'SuperProcInstID', 'WorkObjID', 'WorkObjInfo']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CreateProcInst.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def create_pseudo_work_item(self, **kwargs):
        """Creates a task by a specific AgileWork or other module that has the
        following characteristics:

            * It does not have to be completed in order for a process to advance
                to the next steps.
            * Unless specifically canceled, it remains active through the
                duration of the entire process, not just the duration of the
                AgileWork or other module that created it.

        This provides a way for tasks to be included in a user's or manager's
        task list purely for monitoring purposes.

        Path Args: None
        Required Body Args: bReserved, BusinessTime, ClientData, Length,
                            SourceWorkItemID, Unit, UserID, WorkToPerform
        Optional Body Args: None"""
        req_args = ['bReserved', 'BusinessTime', 'ClientData', 'Length',
                    'SourceWorkItemID', 'Unit', 'UserID', 'WorkToPerform']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CreatePseudoWorkItem.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def create_work_item(self, **kwargs):
        """Creates a manual work item that is linked to another manual work
        item. The work item you create does not depend on the completion of the
        work item to which it is linked. In other words, the original (source)
        work item can be marked as completed before new work item is completed.

        Path Args: None
        Required Body Args: bDependent, BusinessTime, ClientData, Length,
                            SourceWorkItemID, Unit, UserID, WorkToPerform
        Optional Body Args: None"""
        req_args = ['bReserved', 'BusinessTime', 'ClientData', 'Length',
                    'SourceWorkItemID', 'Unit', 'UserID', 'WorkToPerform']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.CreateWorkItem.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def delete_custom_attrs(self, customid):
        """Deletes multiple custom attributes using a custom ID.

        Path Args: customID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.DeleteCustomAttrs(customid).POST()
        return resp.status_code == requests.codes.ok

    def delete_proc_def(self, processtemplateid):
        """Deletes the process definition and all of the process instances
        associated with the process definition. The process definition cannot be
        deleted if one or more process instances associated with the process
        definition is running or suspended. The function may take a long time to
        execute if there are many process instances associated with the process
        definition.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.DeleteProcDef(processtemplateid).POST()
        return resp.status_code == requests.codes.ok

    def delete_proc_inst(self, processinstanceid):
        """Deletes a process instance. This method removes the specified process
        instance and all the associated data from the database, such as work
        items, email, and activity instances associated with this process
        instance. It may take some time to complete this transaction.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.DeleteProcInst(processinstanceid).POST()
        return resp.status_code == requests.codes.ok

    def get_activity_inst(self, activityinstanceid):
        """Retrieves basic information for a specified activity instance.

        Path Args: activityInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetActivityInst(activityinstanceid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_activity_insts_by_p_i_i_d(self, processinstanceid):
        """Retrieves the status of all activity instances for a specified
        process instance.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetActivityInstsByPIID(processinstanceid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_activity_inst_status(self, procinstid):
        """Retrieves all the status of all activity instances for a specified
        process instance.

        Path Args: procInstID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetActivityInstStatus(procinstid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_base_proc_def_i_d(self, procdefname):
        """Retrieves the ID for the first version of the process definition,
        called the base process definition. All subsequent process definition
        versions have the same base process definition ID. This call retrieves
        the base process definition ID with the specified process definition
        name.

        Path Args: procDefName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetBaseProcDefID(procdefname).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_custom_attr(self, customid, **kwargs):
        """Retrieves a single custom attribute.

        Path Args: customID
        Required Body Args: attrName
        Optional Body Args: None"""
        req_args = ['attrName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.GetCustomAttr(customid).POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_custom_attrsby_i_d(self, customid):
        """Gets all the custom attributes with the specified array of custom
        IDs.

        Path Args: customID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetCustomAttrsbyID(customid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_custom_attrs_by_names(self, **kwargs):
        """Retrieves a list of custom attributes using their names or xpaths.

        Path Args: None
        Required Body Args: AttrNames, CustomIDs
        Optional Body Args: None"""
        req_args = ['AttrNames', 'CustomIDs']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.GetCustomAttrsByNames.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_event(self, eventid):
        """Retrieves an event object. This service call is usually used to
        check if a service call has been completed.

        Path Args: eventID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetEvent(eventid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_events_by_proc_inst_i_d(self, processinstanceid):
        """Retrieves all the events that have occurred for a specified process
        instance.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetEventsByProcInstID(processinstanceid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_expecting_send_mail_deliverable(self):  # pylint: disable=invalid-name
        """Retrieves all the failed and scheduled to resend email notifications.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetExpectingSendMailDeliverable.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_mail_deliverables(self):
        """Retrieves all the global email templates from the server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetMailDeliverables.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_def_by_base_pid(self, baseprocesstemplateid):
        """Retrieves all process definitions by a specified base process
        definition ID.

        Path Args: baseprocessTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefByBasePID(baseprocesstemplateid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_def_graphics(self, processid):
        """Retrieves graphical data for the process definition in XML format.
        The graphical representation of the process is XML-serialized by the
        class Graphic Image. The graphical data is used to display the process
        visually.

        Path Args: processID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefGraphics(processid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_def_name_version(self, processtemplateid):
        """Retrieves the process definition name and version.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefNameVersion(processtemplateid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_defs(self):
        """Retrieves all of process definition objects.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefs.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_def_supplement(self, processdefinitionid, activitydefinitionid):
        """Retrieves all the process definition objects and activity objects.

        Path Args: processDefinitionID, activityDefinitionID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefSupplement(
            processdefinitionid)(activitydefinitionid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_def_xml(self, processtemplateid):
        """Retrieves a process definition in XML format.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcDefXml(processtemplateid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_procedure(self, workitemid):
        """Retrieves work item data by a specified work item ID.

        Path Args: workItemID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcedure(workitemid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_inst_attr(self, processinstanceid, attributename):
        """Retrieves a single attribute for a specified process instance.

        Path Args: processInstanceID, attributeName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcInstAttr(
            processinstanceid)(attributename).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_inst_attrs(self, processinstanceid):
        """Retrieves multiple attributes of a process instance.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcInstAttrs(processinstanceid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_proc_inst(self, processinstanceid):
        """Retrieves basic information about a specified process instance.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetProcInst(processinstanceid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_released_p_i_d(self, procdefname):
        """Retrieves the released process definition ID by a specified process
        definition name.

        Path Args: procDefName
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetReleasedPID(procdefname).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_released_proc_defs(self):
        """Retrieves the names and IDs of all released process definitions.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetReleasedProcDefs.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_uuid(self):
        """Retrieves the UUID generated by the AgilePoint Server.

        Path Args: None
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetUUID.GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_work_item(self, workitemid):
        """Retrieves the manual work item object for a specified ID.

        Path Args: workItemID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.GetWorkItem(workitemid).GET()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def get_work_list_by_user_i_d(self, **kwargs):
        """Retrieves a work item collection by specifying a user name and work
        item status.

        Path Args: None
        Required Body Args: Status, UserName
        Optional Body Args: None"""
        req_args = ['Status', 'UserName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.GetWorkListByUserID.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def merge_proc_insts(self, **kwargs):
        """Merges 2 or more process instances into one process instance.

        These process instances should be based on the same process definition.

        http://documentation.agilepoint.com/SupportPortal/DOCS/ProductDocumentation/CurrentRelease/DocumentationLibrary/maps/restmethodMergeProcInsts.html
        Path Args: None
        Required Body Args: MergingProcessInstanceIDs, MergedProcessInstance
        Optional Body Args: None"""
        req_args = ['MergingProcessInstanceIDs', 'MergedProcessInstance']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.MergeProcInsts.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def migrate_proc_inst(self, processinstanceid, reserved='', **kwargs):
        """Migrates a process definition from one version to another version.

        Path Args: processInstanceID, reserved
        Required Body Args: IncludeXmlData, Action, MatchingActivityDefinition,
                            SourceProcessDefinitionID, TargetProcessDefinitionID
        Optional Body Args: None"""
        req_args = ['IncludeXmlData', 'Action', 'MatchingActivityDefinition',
                    'SourceProcessDefinitionID', 'TargetProcessDefinitionID']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.MigrateProcInst(processinstanceid)(
            reserved).POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def query_activity_insts(self, **kwargs):
        """Retrieves activity instances that match a query expression.

        Path Args: None
        Required Body Args: ColumnName, Operator, IsValue
        Optional Body Args: None"""
        req_args = ['ColumnName', 'Operator', 'IsValue']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryActivityInsts.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_audit_trail(self, **kwargs):
        """Retrieves all audit trail items.

        Path Args: None
        Required Body Args: where
        Optional Body Args: None"""
        req_args = ['where']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryAuditTrail.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_database(self, **kwargs):
        """Queries the database with any valid sql query and returns the dataset
        as a string in XML format.

        Path Args: None
        Required Body Args: sql
        Optional Body Args: None"""
        req_args = ['sql']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryDatabase.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_procedure_list(self, **kwargs):
        """Retrieves a list of automatic work items that match a specified query
        expression.

        Path Args: None
        Required Body Args: ColumnName, Operator, WhereClause, IsValue
        Optional Body Args: None"""
        req_args = ['ColumnName', 'Operator', 'WhereClause', 'IsValue']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryProcedureList.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_proc_insts(self, **kwargs):
        """Retrieves a list of process instances that match a specified query
        expression. The WFQueryExpr string is used to generate a query
        expression, and the client application specifies the query terms.

        Path Args: None
        Required Body Args: ColumnName, Operator, IsValue
        Optional Body Args: None"""
        req_args = ['ColumnName', 'Operator', 'IsValue']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryProcInsts.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_proc_insts_using_s_q_l(self, **kwargs):
        """Retrieves a list of process instance based on specified query
        expression.

        Path Args: None
        Required Body Args: sqlWhereClause
        Optional Body Args: None"""
        req_args = ['sqlWhereClause']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryProcInstsUsingSQL.POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_work_list(self, **kwargs):
        """Retrieves a list of manual work items that match a specified query
        expression.

        Path Args: None
        Required Body Args: ColumnName, Operator, WhereClause, IsValue
        Optional Body Args: None"""
        req_args = ['ColumnName', 'Operator', 'WhereClause', 'IsValue']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryWorkList.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def query_work_list_using_s_q_l(self, **kwargs):
        """Retrieves a list of manual work items based on specified query
        expression.

        Path Args: None
        Required Body Args: sqlWhereClause
        Optional Body Args: None"""
        req_args = ['sqlWhereClause']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.QueryWorkListUsingSQL.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def reassign_work_item(self, **kwargs):
        """Reassigns a work item to another participant, and update the user
        name.

        Path Args: None
        Required Body Args: ClientData, UserName, WorkItemID
        Optional Body Args: None"""
        req_args = ['ClientData', 'UserName', 'WorkItemID']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.ReassignWorkItem.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def release_proc_def(self, processtemplateid):
        """Releases a process definition from the AgilePoint Server.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.ReleaseProcDef(processtemplateid).POST()
        return resp.status_code == requests.codes.ok

    def remove_custom_attr(self, customid, **kwargs):
        """Removes a custom attribute from a custom ID.

        Path Args: customID
        Required Body Args: attributeName
        Optional Body Args: None"""
        req_args = ['attributeName']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.RemoveCustomAttr(customid).POST(
            data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def remove_custom_attrs(self, customid, **kwargs):
        """Removes multiple custom attributes from a custom ID.

        Path Args: customID
        Required Body Args: namesArray
        Optional Body Args: None"""
        req_args = ['namesArray']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.RemoveCustomAttrs(customid).POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def resend_mail_deliverable(self, mailid):
        """Resends the mail deliverable with a specified mail ID.

        Path Args: mailID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.ResendMailDeliverable(mailid).POST()
        return resp.status_code == requests.codes.ok

    def restore_proc_inst(self, procinstid):
        """Restores a process instance and associated data from the
        ArchiveDatabase to the AgilePoint Server. The process instance
        records are written to the AgilePoint Database deleted from the
        AgilePoint Archive Database.

        Path Args: procInstID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.RestoreProcInst(procinstid).POST()
        return resp.status_code == requests.codes.ok

    def resume_proc_inst(self, processinstanceid):
        """Resumes a process instance with the specified process instance id.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.ResumeProcInst(processinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def rollback_activity_inst(self, activityinstanceid):
        """Rolls back a manual activity instance to the token position EN -
        that is, the state where the activity is entered. All work items
        associated with the manual activity instance with the status of NEW,
        OVERDUE, or ASSIGNED are canceled.

        Path Args: activityInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.RollbackActivityInst(activityinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def rollback_activity_insts(self, **kwargs):
        """Rolls back a process instance according to a specified instruction.
        The class WFPartialRollbackInstructionis used to specify detailed
        information about the instruction.

        Path Args: None
        Required Body Args: PartialRollbackUnits
        Optional Body Args: None"""
        req_args = ['PartialRollbackUnits']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.RollbackActivityInsts.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def rollback_proc_inst(self, activityinstanceid):
        """Rolls a process instance back to a previous specified activity, or
        skips a specified activity if has not yet been completed. When this
        method is invoked, the current or skipped activity becomes canceled.
        When skipping, the process moves forward regardless of the activity's
        status.

        Path Args: activityInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.RollbackProcInst(activityinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def send_mail(self, **kwargs):
        """Sends an email through AgilePoint Server.

        Path Args: None
        Required Body Args: Attachments, Body, CC, From, Subject, To
        Optional Body Args: None"""
        req_args = ['Attachments, Body, CC, From, Subject, To']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.SendMail.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def set_custom_attrs(self, customid, **kwargs):
        """Sets names and values for multiple custom attributes for a specified
        custom ID.

        Path Args: customID
        Required Body Args: attributes
        Optional Body Args: None"""
        req_args = ['attributes']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.SetCustomAttrs(customid).POST(data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def set_proc_def_supplement(self, processdefinitionid, activitydefinitionid):
        """Sets supplement information related to process definition.

        Path Args: processDefinitionID, activityDefinitionID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.SetProcDefSupplement(
            processdefinitionid)(activitydefinitionid).POST()
        return resp.status_code == requests.codes.ok

    def split_proc_inst(self, **kwargs):
        """Splits one process instance into 2 or more process instances. The
        original process is canceled.

        http://documentation.agilepoint.com/SupportPortal/Docs/ProductDocumentation/05.00.0200/DocumentationLibrary/maps/classWFProcessSplittingInstruction.html

        Path Args: None
        Required Body Args: SplitProcessInstances, SplittingProcessInstanceID
        Optional Body Args: None"""
        req_args = ['SplitProcessInstances', 'SplittingProcessInstanceID']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.SplitProcInst.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def suspend_proc_inst(self, processinstanceid):
        """Suspends a process instance. The process instance status is changed
        to Suspended, and the statuses of all the work items (tasks) become
        Pending.

        Path Args: processInstanceID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.SuspendProcInst(processinstanceid).POST()
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def uncheck_out_proc_def(self, processtemplateid):
        """Undoes a check-out for a process definition. This method returns the
        status of a process definition from CheckedOut to Released without
        making changes to the process definition, or changing the version
        number.

        Path Args: processTemplateID
        Required Body Args: None
        Optional Body Args: None"""
        resp = self.workflow.UnCheckOutProcDef(processtemplateid).POST()
        return resp.status_code == requests.codes.ok

    def undo_assign_work_item(self, workitemid, **kwargs):
        """Unassigns a work item that was previously assigned to a user. This
        method applies to work items that can be assigned to members of task
        groups, where a work item can be assigned to or claimed by any of a
        group of users.

        Path Args: workItemID
        Required Body Args: clientData
        Optional Body Args: None"""
        req_args = ['clientData']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.UndoAssignWorkItem(workitemid).POST(
            data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def update_proc_def(self, **kwargs):
        """Updates a process definition without using version control. This
        method is intended for minor changes only, such as typographical errors.
        Warning: Changes made using this method circumvent version control,
        meaning changes are not tracked, and versions cannot be managed. Do not
        use this call for making any major changes to the process definition.

        Path Args: None
        Required Body Args: xml
        Optional Body Args: None"""
        req_args = ['xml']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.UpdateProcDef.POST(data=json.dumps(kwargs))
        if resp.status_code == requests.codes.ok:
            return resp.json()

    def update_proc_inst(self, processinstanceid, **kwargs):
        """Updates attributes of a workflow process instance. The attributes
        that can be updated are listed in the attribute table.

        Path Args: processInstanceID
        Required Body Args: attributes
        Optional Body Args: None"""
        req_args = ['attributes']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.UpdateProcInst(processinstanceid).POST(
            data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok

    def update_work_item(self, workitemid, **kwargs):
        """Updates a manual work item or automatic work item.

        Path Args: workItemID
        Required Body Args: attributes
        Optional Body Args: None"""
        req_args = ['attributes']
        present_args = kwargs.keys()
        for arg in req_args:
            if arg not in present_args:
                raise MissingRequiredArg(arg)
        resp = self.workflow.UpdateWorkItem(workitemid).POST(
            data=json.dumps(kwargs))
        return resp.status_code == requests.codes.ok
