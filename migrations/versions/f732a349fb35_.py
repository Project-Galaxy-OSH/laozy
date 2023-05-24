"""empty message

Revision ID: f732a349fb35
Revises: 7410e94114ef
Create Date: 2023-05-24 17:38:12.895068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f732a349fb35'
down_revision = '7410e94114ef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('robots', sa.Column('knowledge_max_length', sa.Integer(), nullable=True))
    op.add_column('robots', sa.Column('message_hook', sa.String(length=500), nullable=True))
    op.drop_column('robots', 'knowledge_query_max_length')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('robots', sa.Column('knowledge_query_max_length', sa.INTEGER(), nullable=True))
    op.drop_column('robots', 'message_hook')
    op.drop_column('robots', 'knowledge_max_length')
    # ### end Alembic commands ###