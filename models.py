from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class PortfolioModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class Project(PortfolioModel):
    __tablename__ = "projects"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, default="")
    category: Mapped[str | None] = mapped_column(String(100), default="General")
    tags: Mapped[str | None] = mapped_column(Text, default="")
    image_url: Mapped[str | None] = mapped_column(Text)
    external_url: Mapped[str | None] = mapped_column(Text)


class Skill(PortfolioModel):
    __tablename__ = "skills"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str | None] = mapped_column(String(100), default="Technical")
    proficiency: Mapped[str | None] = mapped_column(String(100), default="Intermediate")
    icon: Mapped[str | None] = mapped_column(String(255), default="fa-solid fa-code")


class Website(PortfolioModel):
    __tablename__ = "websites"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, default="")
    image_url: Mapped[str | None] = mapped_column(Text)
    category: Mapped[str | None] = mapped_column(String(100), default="Portfolio")


class Blog(PortfolioModel):
    __tablename__ = "blogs"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str | None] = mapped_column(Text, default="")
    content: Mapped[str | None] = mapped_column(Text, default="")
    category: Mapped[str | None] = mapped_column(String(100), default="General")
    tags: Mapped[str | None] = mapped_column(Text, default="")
    url: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(Text)


class Certification(PortfolioModel):
    __tablename__ = "certifications"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    issuer: Mapped[str] = mapped_column(String(255), nullable=False)
    issue_date: Mapped[str | None] = mapped_column(String(100))
    credential_url: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(Text)


class CourseLicense(PortfolioModel):
    __tablename__ = "course_licenses"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    institution: Mapped[str] = mapped_column(String(255), nullable=False)
    license_number: Mapped[str | None] = mapped_column(String(255))
    credential_url: Mapped[str | None] = mapped_column(Text)


class Photo(PortfolioModel):
    __tablename__ = "photos"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    caption: Mapped[str | None] = mapped_column(Text, default="")
    image_url: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str | None] = mapped_column(String(100), default="Gallery")


class LinkUrl(PortfolioModel):
    __tablename__ = "link_urls"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    platform: Mapped[str | None] = mapped_column(String(100), default="Web")
    icon: Mapped[str | None] = mapped_column(String(255), default="fa-solid fa-link")


class ContactMessage(PortfolioModel):
    __tablename__ = "contact_messages"

    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(254), nullable=False)
    mobile: Mapped[str | None] = mapped_column(String(50))
    subject: Mapped[str | None] = mapped_column(String(200))
    message: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str | None] = mapped_column(String(50), default="new")
    admin_response: Mapped[str | None] = mapped_column(Text)
    responded_at: Mapped[datetime | None] = mapped_column(DateTime)


class Inquiry(Base):
    __tablename__ = "inquiries"

    record_id: Mapped[str] = mapped_column(String(8), primary_key=True)
    visitor_name: Mapped[str] = mapped_column(String(255), nullable=False)
    visitor_email: Mapped[str] = mapped_column(String(254), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    ml_result: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class AdminUser(PortfolioModel):
    __tablename__ = "admin_users"

    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    password_changed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class AdminSession(PortfolioModel):
    __tablename__ = "admin_sessions"

    user_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime)


class AdminAuditLog(PortfolioModel):
    __tablename__ = "admin_audit_logs"

    user_id: Mapped[int | None] = mapped_column(Integer, index=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(45))
