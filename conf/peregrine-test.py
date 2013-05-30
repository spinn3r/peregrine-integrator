##
#
# build simple/quick peregrine web sources like javadoc/jxr, etc.

SCRATCH="/tmp/integration/test"

TEST_LOGS="/var/lib/integration/peregrine/test"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS=-Xmx512M && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=3 * 60 * 60

TIMEOUT=30*60
