
## AUTOGENERATED.  DO NOT EDIT.

NAME="1:1:1:4"
SCRATCH="/tmp/integration/test-1_1_1_4"

TEST_LOGS="/var/lib/integration/peregrine/test-1_1_1_4"

WEBDIR="/test-1_1_1_4"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=300 -Dmulti.factors=1 -Dmulti.configs=1:1:4' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=12 * 60 * 60

TIMEOUT=30*60

