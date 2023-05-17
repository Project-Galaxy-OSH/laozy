"""message

Revision ID: afed6b329d51
Revises: 17673e044cde
Create Date: 2023-05-09 19:09:09.983242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afed6b329d51'
down_revision = '17673e044cde'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('send_time', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('msgtype', sa.String(length=20), nullable=True))
    op.create_index(op.f('ix_messages_send_time'), 'messages', ['send_time'], unique=False)
    op.drop_column('messages', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('type', sa.VARCHAR(length=20), nullable=True))
    op.drop_index(op.f('ix_messages_send_time'), table_name='messages')
    op.drop_column('messages', 'msgtype')
    op.drop_column('messages', 'send_time')
    # ### end Alembic commands ###
