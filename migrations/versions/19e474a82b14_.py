"""empty message

Revision ID: 19e474a82b14
Revises: 79eda466d680
Create Date: 2023-05-16 16:44:02.516143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19e474a82b14'
down_revision = '79eda466d680'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('created_time', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_channels_created_time'), 'channels', ['created_time'], unique=False)
    op.add_column('prompt_templates', sa.Column('name', sa.String(length=50), nullable=True))
    op.add_column('prompt_templates', sa.Column('owner', sa.String(length=50), nullable=True))
    op.add_column('prompt_templates', sa.Column('created_time', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_prompt_templates_created_time'), 'prompt_templates', ['created_time'], unique=False)
    op.create_index(op.f('ix_prompt_templates_owner'), 'prompt_templates', ['owner'], unique=False)
    op.add_column('robots', sa.Column('name', sa.String(length=50), nullable=True))
    op.add_column('robots', sa.Column('created_time', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_robots_created_time'), 'robots', ['created_time'], unique=False)
    op.create_index(op.f('ix_robots_owner'), 'robots', ['owner'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_robots_owner'), table_name='robots')
    op.drop_index(op.f('ix_robots_created_time'), table_name='robots')
    op.drop_column('robots', 'created_time')
    op.drop_column('robots', 'name')
    op.drop_index(op.f('ix_prompt_templates_owner'), table_name='prompt_templates')
    op.drop_index(op.f('ix_prompt_templates_created_time'), table_name='prompt_templates')
    op.drop_column('prompt_templates', 'created_time')
    op.drop_column('prompt_templates', 'owner')
    op.drop_column('prompt_templates', 'name')
    op.drop_index(op.f('ix_channels_created_time'), table_name='channels')
    op.drop_column('channels', 'created_time')
    # ### end Alembic commands ###
