"""empty message

Revision ID: 7410e94114ef
Revises: 46696f393feb
Create Date: 2023-05-24 17:19:06.557056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7410e94114ef'
down_revision = '46696f393feb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('robots', sa.Column('hisotry_limit', sa.Integer(), nullable=True))
    op.add_column('robots', sa.Column('knowledge_limit', sa.Integer(), nullable=True))
    op.add_column('robots', sa.Column('knowledge_query_limit', sa.Integer(), nullable=True))
    op.add_column('robots', sa.Column('knowledge_query_max_length', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('robots', 'knowledge_query_max_length')
    op.drop_column('robots', 'knowledge_query_limit')
    op.drop_column('robots', 'knowledge_limit')
    op.drop_column('robots', 'hisotry_limit')
    # ### end Alembic commands ###
