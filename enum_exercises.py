from enum import Enum

class OrderStatus(Enum):
    """Enum representing order status."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    PREPARING = "Preparing"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class Order:
    """Class to handle order status transitions."""
    def __init__(self, order_id):
        """Initialize Order instance."""
        self.order_id = order_id
        self.status = OrderStatus.PENDING

    def update_status(self, new_status):
        """Update order status."""
        if self.status == OrderStatus.CANCELLED or self.status == OrderStatus.DELIVERED:
            print("Cannot update status. Order is already cancelled or delivered.")
            return

        # Check if the transition is valid
        if self._is_valid_transition(new_status):
            self.status = new_status
            print(f"Order {self.order_id} status updated to {new_status.value}")
        else:
            print(f"Invalid status transition from {self.status.value} to {new_status.value}")

    def _is_valid_transition(self, new_status):
        """Check if the transition to the new status is valid."""
        # Define valid transitions
        valid_transitions = {
            OrderStatus.PENDING: {OrderStatus.CONFIRMED},
            OrderStatus.CONFIRMED: {OrderStatus.PREPARING, OrderStatus.CANCELLED},
            OrderStatus.PREPARING: {OrderStatus.OUT_FOR_DELIVERY, OrderStatus.CANCELLED},
            OrderStatus.OUT_FOR_DELIVERY: {OrderStatus.DELIVERED},
            OrderStatus.DELIVERED: {},
            OrderStatus.CANCELLED: {}
        }

        # Check if the transition is valid
        return new_status in valid_transitions.get(self.status, {})

# Create an order with order ID 123
order = Order(123)

# Simulate order lifecycle
order.update_status(OrderStatus.CONFIRMED)  # Transition: Pending -> Confirmed
order.update_status(OrderStatus.PREPARING)  # Transition: Confirmed -> Preparing
order.update_status(OrderStatus.OUT_FOR_DELIVERY)  # Transition: Preparing -> Out for Delivery
order.update_status(OrderStatus.DELIVERED)  # Transition: Out for Delivery -> Delivered

# Trying to update status after delivery
order.update_status(OrderStatus.PREPARING)  # Should print "Cannot update status. Order is already delivered."
