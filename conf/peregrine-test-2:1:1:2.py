
## AUTOGENERATED.  DO NOT EDIT.
SCRATCH="/tmp/integration/test-2:1:1:2"

TEST_LOGS="/var/lib/integration/peregrine/test-2:1:1:2"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS=-Xmx512M -Dperegrine.test.portOffset=550 -Dmulti.factors=2 -Dmulti.configs=1:1:2 && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=3 * 60 * 60

TIMEOUT=30*60

