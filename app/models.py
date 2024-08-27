from pydantic import BaseModel
from typing import List, Optional

class TheaterData(BaseModel):
    theater_code: str
    screen_name: str
    screen_screened: Optional[str]
    screen_fiscal_year: Optional[str]
    screen_capacity: Optional[int]
    screen_rows: Optional[int]
    screen_columns: Optional[int]
    screen_vertical_start: Optional[int]
    screen_horizontal_start: Optional[int]
    screen_disable_seats: Optional[int]
    screen_ticket: Optional[str]

class TicketDetails(BaseModel):
    theater_code: str
    screen_name: str
    screened: Optional[str]
    show_type_name: Optional[str]
    show_typed: Optional[str]
    movie_name: Optional[str]
    movie_code: Optional[str]
    fiscal_year: Optional[str]
    show_date_time: Optional[str]
    showed: Optional[str]
    ticket_print_date_time: Optional[str]
    ticket_type_name: Optional[str]
    ticket_typed: Optional[str]
    payment_type_name: Optional[str]
    payment_typed: Optional[str]
    ticket_code: Optional[str]
    seat_number: Optional[str]
    ticket_status_name: Optional[str]
    ticket_status_value: Optional[str]
    ticket_net_price: Optional[float]
    ticket_price: Optional[float]
    ticket_tax: Optional[float]
    ticket_charge: Optional[float]
    distributor_code: Optional[str]
    distributor_commission_value: Optional[float]
    is_real_time: Optional[bool]

class ReturnTicketDetails(BaseModel):
    show_date_time: str
    ref_ticket_code: str
    ticket_cancelled_reason: Optional[str]
    ticket_cancelled_date_time: Optional[str]
    ticket_net_price: Optional[float]
    ticket_price: Optional[float]
    ticket_tax: Optional[float]
    ticket_charge: Optional[float]
    is_real_time: Optional[bool]
    theater_code: str
    fiscal_year: Optional[str]
    showed: Optional[str]

class ShowDetails(BaseModel):
    theater_code: str
    fiscal_year: Optional[str]
    showed: Optional[str]
    show_status: Optional[str]
    show_date_time: Optional[str]
    show_added_date_time: Optional[str]
    is_real_time: Optional[bool]

class CancelShowDetails(BaseModel):
    theater_code: str
    fiscal_year: Optional[str]
    showed: Optional[str]
    show_date_time: Optional[str]
    show_cancelled_reason: Optional[str]
    show_cancelled_date_time: Optional[str]
    is_real_time: Optional[bool]
