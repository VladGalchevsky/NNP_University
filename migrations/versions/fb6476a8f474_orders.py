"""orders

Revision ID: fb6476a8f474
Revises: c3707d1c59e3
Create Date: 2024-09-12 07:18:26.682409

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb6476a8f474'
down_revision: Union[str, None] = 'c3707d1c59e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.UUID(), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=False),
    sa.Column('total_price', sa.FLOAT(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('order_status', sa.Enum('PENDING', 'SHIPPED', 'DELIVERED', 'CANCELED', 'DELETED', name='orderstatusenum'), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_index(op.f('ix_users_is_active'), 'users', ['is_active'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_is_active'), table_name='users')
    op.drop_table('orders')
    # ### end Alembic commands ###
