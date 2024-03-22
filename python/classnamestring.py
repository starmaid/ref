def _getClassNameString(obj):
    # This function turns the classname into a string
    # so that the import can load the class easily.
    # this is kindof a workaround and should be handled further 
    # on the destination side.
    basestring = str(type(obj))
    tailstring = basestring.split('.')[-1].replace('\'>','').replace('<class \'','')
    return tailstring

instance = {}

# verbose print
#print(f'Read {type(d)}: {str(d)}')

fieldList = [f.name for f in d._meta.local_fields]

for f in fieldList:
    # handle all fields
    a = getattr(d, f)
    
    instance[f'{f}_type'] = _getClassNameString(a)
    
    if (isinstance(a, str) or isinstance(a, dict)
        or isinstance(a, int) or isinstance(a, float) 
        or isinstance(a, bool) or isinstance(a, list) 
        or isinstance(a, type(None))):
        # json-compatible types
        instance[f] = a
    elif (isinstance(a, datetime) or 
          isinstance(a, timedelta) or 
          isinstance(a, date) or
          isinstance(a, UUID) or
          isinstance(a, Decimal)):
        # non-lossy string conversions
        # fun fact the decimal type is nonlossy as a string
        instance[f] = str(a)
    elif isinstance(a, Project):
        instance[f] = str(a.uuid)
        instance[f + '_name'] = str(a.name)
    elif isinstance(a, User):
        instance[f] = str(a.uuid)
        instance[f + '_email'] = str(a.email)
    elif isinstance(a, ProjectRoute):
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
        self._createPRouteEntry(a)
    elif isinstance(a, ExperimentRoute):
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
        self._createERouteEntry(a)
    elif (isinstance(a, Process) or 
        isinstance(a, Experiment) or 
        isinstance(a, ExperimentExecutionStep)):
        # just put the uuid (dont recurse!)
        # Process is found inside Experiment
        # Experiment is found inside Note
        # ExperimentExecutionStep found in SJAnalysisData
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
    elif isinstance(a, DeviceTimeSlot):
        # need these to display experiments properly.
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
        self._createDeviceTimeSlotEntry(a)
    elif isinstance(a, ExperimentExecution):
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
        
        if not (isinstance(d, ExperimentExecutionStep) or
                isinstance(d, AnalysisData)):
            # ExperimentExecution found inside ExperimentExecutionStep and AnalysisData
            self._createExpExecutionEntry(a)
    elif isinstance(a, ExperimentResult):
        instance[f] = str(a)
        instance[f + '_id'] = str(a.uuid)
        
        if not isinstance(d, ExperimentResultAttachment):
            # result and result attachment link to each other! 
            # stop recursing!
            self._createExpResultEntry(a)
    elif isinstance(a, FieldFile):
        instance[f] = str(a.path)
        instance[f + '_name'] = str(a.name)
        self._createFileEntry(a)
    elif isinstance(a, ExecutionLog):
        # hmmm i dont really care about taking the log file
        instance[f] = None
    
    else:
        # TODO: remove this print and make it error once we handle all these
        print(f'Unknown type {type(a)} encountered. please update code')
