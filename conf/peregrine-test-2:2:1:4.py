
## AUTOGENERATED.  DO NOT EDIT.
SCRATCH="/tmp/integration/test-2_2_1_4"

TEST_LOGS="/var/lib/integration/peregrine/test-2_2_1_4"

TEST_COMMAND="export HOSTNAME=localhost && export ANT_OPTS='-Xmx512M -Dperegrine.test.portOffset=750 -Dmulti.factors=2 -Dmulti.configs=2:1:4' && time ant test"

POST_COMMAND="export ANT_OPTS=-Xmx512M && ant test-report"

REPO="https://burtonator:redapplekittycat@bitbucket.org/burtonator/peregrine"

OUTPUT = { 'test-reports' : 'target/test-reports'  }

OLD_AGE=24 * 60 * 60

TIMEOUT=30*60

