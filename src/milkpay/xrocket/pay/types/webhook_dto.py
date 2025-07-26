from datetime import datetime
from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject


class WebhookPaymentDto(PayXRocketObject):
    user_id: Union[int, float] = Field(alias="userId")
    """User ID who made the payment"""
    payment_num: Union[int, float] = Field(alias="paymentNum")
    """Payment number"""
    paid: datetime
    """When payment was made"""
    payment_amount: Union[int, float] = Field(alias="paymentAmount")
    """Payment amount"""
    payment_amount_received: Union[int, float] = Field(alias="paymentAmountReceived")
    """Payment amount received after fees"""


class WebhookInvoiceDataDto(PayXRocketObject):
    id: str
    """Invoice ID"""
    amount: Union[int, float]
    """Invoice amount"""
    min_payment: Optional[Union[int, float]] = Field(default=None, alias="minPayment")
    """Minimum payment amount"""
    currency: str
    """Currency code"""
    description: Optional[str] = None
    """Invoice description"""
    hidden_message: Optional[str] = Field(default=None, alias="hiddenMessage")
    """Hidden message"""
    payload: str
    """Invoice payload"""
    callback_url: str = Field(alias="callbackUrl")
    """Callback URL"""
    created: datetime
    """When invoice was created"""
    paid: datetime
    """When invoice was paid"""
    status: str
    """Invoice status"""
    expired_in: Union[int, float] = Field(alias="expiredIn")
    """Expiration time in seconds"""
    link: str
    """Invoice link"""
    activations_left: Union[int, float] = Field(alias="activationsLeft")
    """Activations left"""
    total_activations: Union[int, float] = Field(alias="totalActivations")
    """Total activations"""
    payment: WebhookPaymentDto
    """Payment details"""


class WebhookDto(PayXRocketObject):
    type: str
    """type of webhook sent"""
    timestamp: datetime
    """When webhook was sent"""
    data: WebhookInvoiceDataDto
    """Webhook data with invoice information"""
