# mewcode-alert-demo

Throwaway repository for demonstrating MewCode's alert-driven fix pipeline.
Planted bug: `null_deref`.

Has a docker-compose dependency (`cache`) and an integration test that
only passes when the service layer starts it (M2 W4).
