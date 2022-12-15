import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


sentry_sdk.init(
    dsn="https://6f6dd5b2d306491c9d3818fd52dcf6f1@o4504333296205824.ingest.sentry.io/4504333307215872",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
