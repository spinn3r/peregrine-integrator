##
#
# build simple/quick peregrine web sources like javadoc/jxr, etc.

SCRATCH="/tmp/integration/test"

TEST_LOGS="/var/lib/integration/peregrine/test"

TEST_COMMAND="export ANT_OPTS=-Xmx512M && time ant test"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }
