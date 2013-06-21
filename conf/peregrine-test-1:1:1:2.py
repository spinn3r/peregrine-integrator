
## AUTOGENERATED.  DO NOT EDIT.

NAME="T:1:1:1:2"
SCRATCH="/tmp/integration/test-1_1_1_2"

TEST_LOGS="/var/lib/integration/peregrine/test-1_1_1_2"

WEBDIR="/test-1_1_1_2"

TEST_COMMAND="ulimit -n 100000 && export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.backend=threads -Dperegrine.test.portOffset=250 -Dmulti.factors=1 -Dmulti.configs=1:1:2' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=1 * 60 * 60

TIMEOUT=30*60

