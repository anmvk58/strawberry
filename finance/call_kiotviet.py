import pandas as pd
from datetime import datetime
from make_df_shipper import make_shipper
import numpy as np

filename = datetime.today().strftime('%Y%m%d')
# filename = "20231230_test"
KIOT_PATH = "C:\\Users\\AnMV\\Desktop\\Temp\\Dâu\\{}.xlsx".format(filename)
SHIP_PATH = "C:\\Users\\AnMV\\Desktop\\Temp\\\Dâu\\input_ship.txt"

def calculate_for_one_ship(df, shipper_name):
    df_notchuyenkhoan = df.loc[df['CK'] != 'C']
    tong_tien = sum(df_notchuyenkhoan['Tổng tiền hàng'])
    tong_don = df.shape[0]
    tien_ship = tong_don*25000
    phai_thu = tong_tien - tien_ship

    data = [['Tổng tiền', tong_tien], ['Tiền ship', tien_ship], ['Cắt ship', 0], ['Phải thu', phai_thu]]
    df_result = pd.DataFrame(data, columns=['Shipper', shipper_name])
    return df_result

if __name__ == '__main__':
    df_shipper = make_shipper(SHIP_PATH)

    df_kiotviet = pd.read_excel(KIOT_PATH)

    df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="left")

    list_shipper = df_shipper['Shipper'].unique()

    # Duplicate column
    df_total['Total money'] = df_total.loc[:, 'Tổng tiền hàng']
    # Reorder column
    df_total = df_total[['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper', 'CK', 'Tổng tiền hàng', 'Total money']]

    df_total["Tổng tiền hàng"] = np.where(df_total["CK"] == "C", 0, df_total["Tổng tiền hàng"])

    writer = pd.ExcelWriter(f"C:\\Users\\AnMV\\Desktop\\Temp\\Dâu\\{filename}_result.xlsx", engine='xlsxwriter')
    df_total.to_excel(writer, sheet_name='Invoices', index=False)

    total_shipper_df = pd.DataFrame()

    for ship in list_shipper:
        df_ship = df_total.loc[df_total['Shipper'] == ship]
        df_cal = calculate_for_one_ship(df_ship, ship)

        total_shipper_df = pd.concat([total_shipper_df, df_cal], axis=1)

        df_cal.to_excel(writer, sheet_name=ship, index=False, startrow=0, startcol=0)
        df_ship.to_excel(writer, sheet_name=ship, index=False, startrow=df_cal.shape[0] + 2, startcol=0)

        # print(df_cal)
        print("---")

    total_shipper_df.to_excel(writer, sheet_name="Total", index=False, startrow=df_cal.shape[0] + 2, startcol=0)
    writer.close()
    print('a')
