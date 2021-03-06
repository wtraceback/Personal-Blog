"""update comment table and post table

Revision ID: 890971f00560
Revises: 5fafaa9e5887
Create Date: 2020-11-19 20:53:13.861443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '890971f00560'
down_revision = '5fafaa9e5887'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('reviewed', sa.Boolean(), nullable=True))
    op.add_column('post', sa.Column('can_comment', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'can_comment')
    op.drop_column('comment', 'reviewed')
    # ### end Alembic commands ###
