from src.tax import vat
from src.sale import sale
from src.unique_products import unique_products


def main():
    taxes = vat()
    sale_amount = sale()
    unique = unique_products()
    print('VAT:', taxes,'€\nSale:', sale_amount, '€\nUnique products:', unique)


if __name__ == "__main__":
    main()