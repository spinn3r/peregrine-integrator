
## AUTOGENERATED.  DO NOT EDIT.

NAME="1:2:1:1"
SCRATCH="/tmp/integration/test-1_2_1_1"

TEST_LOGS="/var/lib/integration/peregrine/test-1_2_1_1"

WEBDIR="/test-1_2_1_1"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=400 -Dmulti.factors=1 -Dmulti.configs=2:1:1' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=7 * 24 * 60 * 60

TIMEOUT=30*60

