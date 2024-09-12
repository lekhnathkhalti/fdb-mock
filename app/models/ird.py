from datetime import datetime
from pydantic import BaseModel


class Bill(BaseModel):
    username: str
    password: str
    seller_pan: str
    buyer_pan: str
    fiscal_year: str
    buyer_name: str
    invoice_number: str
    invoice_date: str
    total_sales: float
    taxable_sales_vat: float
    vat: float
    excisable_amount: float
    excise: float
    taxable_sales_hst: float
    hst: float
    amount_for_esf: float
    esf: float
    export_sales: float
    tax_exempted_sales: float
    isrealtime: bool
    datetimeClient: datetime


class BillReturn(Bill):
    ref_invoice_number: str
    credit_note_number: str
    credit_note_date: str
    reason_for_return: str
