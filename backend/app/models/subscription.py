from __future__ import annotations

import enum
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class SubscriptionPlan(str, enum.Enum):
    FREE = "FREE"
    PRO = "PRO"
    EXECUTIVE = "EXECUTIVE"
    ENTERPRISE = "ENTERPRISE"


class SubscriptionProvider(str, enum.Enum):
    APPLE = "APPLE"
    GOOGLE = "GOOGLE"
    STRIPE = "STRIPE"


class Subscription(BaseModel):
    __tablename__ = "subscriptions"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    plan: Mapped[SubscriptionPlan] = mapped_column(
        Enum(SubscriptionPlan, name="subscription_plan"),
        server_default=SubscriptionPlan.FREE.value,
    )
    status: Mapped[str] = mapped_column(String(64))
    provider: Mapped[SubscriptionProvider] = mapped_column(
        Enum(SubscriptionProvider, name="subscription_provider"),
    )
    provider_subscription_id: Mapped[str | None] = mapped_column(String(255))
    current_period_end: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))

    __table_args__ = (Index("ix_subscriptions_user_id", "user_id"),)
