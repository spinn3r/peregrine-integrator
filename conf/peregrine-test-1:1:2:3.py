
## AUTOGENERATED.  DO NOT EDIT.
SCRATCH="/tmp/integration/test-1:1:2:3"

TEST_LOGS="/var/lib/integration/peregrine/test-1:1:2:3"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS=-Xmx512M -Dperegrine.test.portOffset=350 -Dmulti.factors=1 -Dmulti.configs=1:2:3 && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=24 * 60 * 60

TIMEOUT=30*60

