
## AUTOGENERATED.  DO NOT EDIT.

NAME="2:1:1:1"
SCRATCH="/tmp/integration/test-2_1_1_1"

TEST_LOGS="/var/lib/integration/peregrine/test-2_1_1_1"

WEBDIR="/test-2_1_1_1"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=500 -Dmulti.factors=2 -Dmulti.configs=1:1:1' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=12 * 60 * 60

TIMEOUT=30*60

