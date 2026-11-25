"""create aegis ai tables

Revision ID: 0001_create_aegis_ai_tables
Revises: 
Create Date: 2026-06-03
"""

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0001_create_aegis_ai_tables"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column("firebase_uid", sa.String(length=128), nullable=False, unique=True),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("full_name", sa.String(length=255)),
        sa.Column("avatar_url", sa.String(length=500)),
        sa.Column(
            "role",
            sa.Enum("USER", "ADMIN", "SUPER_ADMIN", name="user_role"),
            nullable=False,
            server_default="USER",
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("timezone", sa.String(length=64)),
        sa.Column("locale", sa.String(length=32)),
    )
    op.create_index("ix_users_email", "users", ["email"])
    op.create_index("ix_users_firebase_uid", "users", ["firebase_uid"])

    op.create_table(
        "conversation_sessions",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=255)),
    )
    op.create_index(
        "ix_conversation_sessions_user_id",
        "conversation_sessions",
        ["user_id"],
    )

    op.create_table(
        "user_preferences",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("preferred_working_hours_start", sa.Time()),
        sa.Column("preferred_working_hours_end", sa.Time()),
        sa.Column("preferred_meeting_duration", sa.Integer()),
        sa.Column("commute_home_address", sa.String(length=255)),
        sa.Column("commute_work_address", sa.String(length=255)),
        sa.Column(
            "communication_style",
            sa.Enum("FORMAL", "CASUAL", name="communication_style"),
        ),
        sa.Column("notification_lead_time_minutes", sa.Integer()),
        sa.Column("preferred_travel_mode", sa.String(length=64)),
    )
    op.create_index("ix_user_preferences_user_id", "user_preferences", ["user_id"])

    op.create_table(
        "calendar_connections",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "provider",
            sa.Enum("GOOGLE", "OUTLOOK", name="calendar_provider"),
            nullable=False,
        ),
        sa.Column("access_token", sa.String(length=2048), nullable=False),
        sa.Column("refresh_token", sa.String(length=2048)),
        sa.Column("token_expiry", sa.DateTime(timezone=True)),
        sa.Column("calendar_id", sa.String(length=255)),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
    )
    op.create_index(
        "ix_calendar_connections_user_id",
        "calendar_connections",
        ["user_id"],
    )

    op.create_table(
        "email_connections",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("provider", sa.String(length=32), server_default="GMAIL"),
        sa.Column("access_token", sa.String(length=2048), nullable=False),
        sa.Column("refresh_token", sa.String(length=2048)),
        sa.Column("token_expiry", sa.DateTime(timezone=True)),
        sa.Column("scopes", postgresql.JSONB()),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
    )
    op.create_index(
        "ix_email_connections_user_id",
        "email_connections",
        ["user_id"],
    )

    op.create_table(
        "meetings",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("google_event_id", sa.String(length=255)),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("start_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("end_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("location", sa.String(length=255)),
        sa.Column(
            "status",
            sa.Enum(
                "SCHEDULED",
                "CANCELLED",
                "RESCHEDULED",
                "COMPLETED",
                name="meeting_status",
            ),
            nullable=False,
            server_default="SCHEDULED",
        ),
        sa.Column("attendees", postgresql.JSONB()),
        sa.Column("meeting_link", sa.String(length=500)),
        sa.Column("recurrence_rule", sa.String(length=500)),
        sa.Column("timezone", sa.String(length=64)),
    )
    op.create_index("ix_meetings_user_id", "meetings", ["user_id"])
    op.create_index("ix_meetings_user_start", "meetings", ["user_id", "start_time"])

    op.create_table(
        "tasks",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("due_date", sa.DateTime(timezone=True)),
        sa.Column(
            "priority",
            sa.Enum("LOW", "MEDIUM", "HIGH", "URGENT", name="task_priority"),
            nullable=False,
            server_default="MEDIUM",
        ),
        sa.Column(
            "status",
            sa.Enum(
                "TODO",
                "IN_PROGRESS",
                "DONE",
                "CANCELLED",
                name="task_status",
            ),
            nullable=False,
            server_default="TODO",
        ),
        sa.Column("tags", postgresql.JSONB()),
        sa.Column(
            "related_meeting_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("meetings.id", ondelete="SET NULL"),
        ),
    )
    op.create_index("ix_tasks_user_id", "tasks", ["user_id"])
    op.create_index("ix_tasks_related_meeting_id", "tasks", ["related_meeting_id"])

    op.create_table(
        "travel_plans",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("origin", sa.String(length=255), nullable=False),
        sa.Column("destination", sa.String(length=255), nullable=False),
        sa.Column("departure_time", sa.DateTime(timezone=True)),
        sa.Column("arrival_time", sa.DateTime(timezone=True)),
        sa.Column("travel_mode", sa.String(length=64)),
        sa.Column("distance_meters", sa.Integer()),
        sa.Column("duration_seconds", sa.Integer()),
        sa.Column("traffic_duration_seconds", sa.Integer()),
        sa.Column("route_polyline", sa.String(length=2048)),
        sa.Column(
            "related_meeting_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("meetings.id", ondelete="SET NULL"),
        ),
    )
    op.create_index("ix_travel_plans_user_id", "travel_plans", ["user_id"])
    op.create_index(
        "ix_travel_plans_related_meeting_id",
        "travel_plans",
        ["related_meeting_id"],
    )

    op.create_table(
        "agent_memories",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "memory_type",
            sa.Enum("PREFERENCE", "FACT", "PATTERN", "EVENT", name="memory_type"),
            nullable=False,
        ),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("embedding", Vector(1536)),
        sa.Column("metadata", postgresql.JSONB()),
        sa.Column("importance_score", sa.Float()),
        sa.Column("last_accessed_at", sa.DateTime(timezone=True)),
    )
    op.create_index("ix_agent_memories_user_id", "agent_memories", ["user_id"])
    op.create_index(
        "ix_agent_memories_embedding",
        "agent_memories",
        ["embedding"],
        postgresql_using="ivfflat",
        postgresql_ops={"embedding": "vector_cosine_ops"},
    )

    op.create_table(
        "notifications",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "type",
            sa.Enum(
                "MEETING_REMINDER",
                "DEPARTURE_ALERT",
                "EMAIL_RECEIVED",
                "TASK_DUE",
                "SYSTEM",
                name="notification_type",
            ),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("data", postgresql.JSONB()),
        sa.Column("is_read", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("scheduled_for", sa.DateTime(timezone=True)),
        sa.Column("sent_at", sa.DateTime(timezone=True)),
    )
    op.create_index("ix_notifications_user_id", "notifications", ["user_id"])

    op.create_table(
        "subscriptions",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "plan",
            sa.Enum("FREE", "PRO", "EXECUTIVE", "ENTERPRISE", name="subscription_plan"),
            nullable=False,
            server_default="FREE",
        ),
        sa.Column("status", sa.String(length=64), nullable=False),
        sa.Column(
            "provider",
            sa.Enum("APPLE", "GOOGLE", "STRIPE", name="subscription_provider"),
            nullable=False,
        ),
        sa.Column("provider_subscription_id", sa.String(length=255)),
        sa.Column("current_period_end", sa.DateTime(timezone=True)),
    )
    op.create_index("ix_subscriptions_user_id", "subscriptions", ["user_id"])

    op.create_table(
        "device_tokens",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "platform",
            sa.Enum("IOS", "ANDROID", "WEB", name="device_platform"),
            nullable=False,
        ),
        sa.Column("token", sa.String(length=512), nullable=False, unique=True),
    )
    op.create_index("ix_device_tokens_user_id", "device_tokens", ["user_id"])
    op.create_index("ix_device_tokens_token", "device_tokens", ["token"])

    op.create_table(
        "audit_logs",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
        ),
        sa.Column("action", sa.String(length=128), nullable=False),
        sa.Column("resource_type", sa.String(length=128), nullable=False),
        sa.Column("resource_id", sa.String(length=128)),
        sa.Column("old_value", postgresql.JSONB()),
        sa.Column("new_value", postgresql.JSONB()),
        sa.Column("ip_address", sa.String(length=64)),
        sa.Column("user_agent", sa.Text()),
    )
    op.create_index("ix_audit_logs_user_id", "audit_logs", ["user_id"])

    op.create_table(
        "messages",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("version", sa.Integer(), server_default=sa.text("1")),
        sa.Column(
            "session_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("conversation_sessions.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "role",
            sa.Enum("USER", "ASSISTANT", "TOOL", name="message_role"),
            nullable=False,
        ),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("token_count", sa.Integer()),
        sa.Column("model_used", sa.String(length=128)),
    )
    op.create_index("ix_messages_session_id", "messages", ["session_id"])
    op.create_index("ix_messages_user_id", "messages", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_messages_user_id", table_name="messages")
    op.drop_index("ix_messages_session_id", table_name="messages")
    op.drop_table("messages")

    op.drop_index("ix_audit_logs_user_id", table_name="audit_logs")
    op.drop_table("audit_logs")

    op.drop_index("ix_device_tokens_token", table_name="device_tokens")
    op.drop_index("ix_device_tokens_user_id", table_name="device_tokens")
    op.drop_table("device_tokens")

    op.drop_index("ix_subscriptions_user_id", table_name="subscriptions")
    op.drop_table("subscriptions")

    op.drop_index("ix_notifications_user_id", table_name="notifications")
    op.drop_table("notifications")

    op.drop_index("ix_agent_memories_embedding", table_name="agent_memories")
    op.drop_index("ix_agent_memories_user_id", table_name="agent_memories")
    op.drop_table("agent_memories")

    op.drop_index("ix_travel_plans_related_meeting_id", table_name="travel_plans")
    op.drop_index("ix_travel_plans_user_id", table_name="travel_plans")
    op.drop_table("travel_plans")

    op.drop_index("ix_tasks_related_meeting_id", table_name="tasks")
    op.drop_index("ix_tasks_user_id", table_name="tasks")
    op.drop_table("tasks")

    op.drop_index("ix_meetings_user_start", table_name="meetings")
    op.drop_index("ix_meetings_user_id", table_name="meetings")
    op.drop_table("meetings")

    op.drop_index("ix_email_connections_user_id", table_name="email_connections")
    op.drop_table("email_connections")

    op.drop_index("ix_calendar_connections_user_id", table_name="calendar_connections")
    op.drop_table("calendar_connections")

    op.drop_index("ix_user_preferences_user_id", table_name="user_preferences")
    op.drop_table("user_preferences")

    op.drop_index(
        "ix_conversation_sessions_user_id",
        table_name="conversation_sessions",
    )
    op.drop_table("conversation_sessions")

    op.drop_index("ix_users_firebase_uid", table_name="users")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")

    op.execute("DROP EXTENSION IF EXISTS vector")
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp"')
