
## AUTOGENERATED.  DO NOT EDIT.

NAME="2:1:2:3"
SCRATCH="/tmp/integration/test-2_1_2_3"

TEST_LOGS="/var/lib/integration/peregrine/test-2_1_2_3"

WEBDIR="/test-2_1_2_3"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=650 -Dmulti.factors=2 -Dmulti.configs=1:2:3' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=3 * 24 * 60 * 60

TIMEOUT=30*60

