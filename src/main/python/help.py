# THIS FILE IS AUTOGENERATED

def print_help ():
    print 'Version: 3.0.1 2013-06-03'
    print
    print 'Usage:'
    print
    print 'ofexport [options...] -o file_name'
    print
    print 'options:'
    print '  -h,-?,--help       : print help'
    print '  -C                 : context mode (as opposed to project mode)'
    print '  -P                 : project mode - the default (as opposed to context mode)'
    print '  -I                 : include mode (as opposed to exclude mode)'
    print '  -E                 : exclude mode - the default (as opposed to include mode)'
    print '  -o file_name       : the output file name, must end in a recognised suffix - see documentation'
    print '  -i file_name       : read file_name instead of the OmniFocus database, must be in json format'
    print '  -T template_name   : use the specified template instead of one derived from the output file extension'
    print '  --open             : open the output file with the registered application (if one is installed)'
    print '  -v                 : verbose output'
    print '  -z                 : maximum diagnostics'
    print '  -V level           : set the global log level (ERROR, INFO, DEBUG, TRACE)'
    print '  --log name=level   : set a logger to a particular level'
    print '  --debug arg        : set test options'
    print
    print 'filters:'
    print '  -a,--any expr        : filter tasks, projects, contexts and folders against the expression'
    print '  -t,--task expr       : filter any task against task against the expression'
    print '  -p,--project expr    : filter any project against the expression'
    print '  -f,--folder expr     : filter any folder against the expression'
    print '  -c,--context expr    : filter any context type against the expression'
    print '  --tasks              : filter out everything except tasks'
    print
    print '  See DOCUMENTATION.md for more information'

SHORT_OPTS = 'h?CPIEo:i:T:vzV:a:t:p:f:c:'
LONG_OPTS = ['help','open','log=','debug=','any=','task=','project=','folder=','context=','tasks']
