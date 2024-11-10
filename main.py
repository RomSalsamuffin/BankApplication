from src.masks import get_masks_account, get_masks_card_number
from src.widget import get_date, masks_account_card

print(get_masks_card_number(7000792289606361))

print(get_masks_account(73654108430135874305))

print(get_date("2024-03-11T02:26:18.671407"))

print(masks_account_card('Maestro 1596837868705199'))

