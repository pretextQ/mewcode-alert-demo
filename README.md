# mewcode-alert-demo

Throwaway repository for demonstrating MewCode's alert-driven fix pipeline.
Planted bug: `unhandled_timeout`.

Has a docker-compose dependency (`cache`) and an integration test that
only passes when the service layer starts it (M2 W4).
