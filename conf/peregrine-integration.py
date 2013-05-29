##
#
# build simple/quick peregrine web sources like javadoc/jxr, etc.


SCRATCH="/tmp/integration/peregrine/integration"

TEST_LOGS="/var/lib/integration/peregrine/integration"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS=-Xmx512M && ant clean jar compile.test jar && time ant integrate"

###
# specify a post command to use AFTER we run our test.
POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports' }
