## AUTOGENERATED.  DO NOT EDIT.

NAME="core"
SCRATCH="/tmp/integration/test-core"

TEST_LOGS="/var/lib/integration/peregrine/test-core"

WEBDIR="/test-core"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=50' && time ant core"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=3 * 24 * 60 * 60

TIMEOUT=30*60

