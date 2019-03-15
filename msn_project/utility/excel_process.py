import datetime
import os
import numpy as np
import pandas as pd

from msn_project.utility.db_models import db

DOWNLOAD_BASE_PATH = r"D:\work\Pycharm_Projects\msn_tool_relationdocuments"

def duomai_import(filename):
    filepath = os.path.join(DOWNLOAD_BASE_PATH, filename)
    df = pd.read_csv(filepath, header=[0])
    lastIndex = len(df) - 1
    if np.isnan(df.ix[lastIndex,1]):
        df = df.drop([lastIndex])
    df.columns = [
        'vip_id',
        'website_id',
        'activity_id',
        'order_time',
        'feedback_label',
        'order_number',
        'intention_order_number',
        'intention_order_amount',
        'intention_commission',
        'confirmed_order_number',
        'confirmed_order_amount',
        'confirmed_commission',
        'performance_status',
        'performance_confirmed_time']
    df['create_time'] = datetime.datetime.now()
    df['modify_time'] = datetime.datetime.now()

    df[['vip_id', 'website_id', 'intention_order_number', 'confirmed_order_number']] = \
        df[['vip_id', 'website_id', 'intention_order_number', 'confirmed_order_number']].astype(int, errors='ignore')

    df[['intention_order_amount', 'intention_commission', 'confirmed_order_amount', 'confirmed_commission']] = \
        df[['intention_order_amount', 'intention_commission', 'confirmed_order_amount', 'confirmed_commission']] \
            .astype(float, errors='ignore')

    df[['feedback_label', 'performance_status', 'order_number', 'activity_id']] = \
        df[['feedback_label', 'performance_status', 'order_number', 'activity_id']] \
            .apply(lambda x: '' if str(x) == 'nan' else x)

    df[["order_time", 'performance_confirmed_time', 'create_time', 'modify_time']] = \
        pd.to_datetime(df[["order_time", 'performance_confirmed_time', 'create_time', 'modify_time']].stack()).unstack()

    df.to_sql(name='duomai_report_details', con=db.engine, if_exists='append', index=False)
    print('import successful !')


def taobao_import(filename):
    filepath = os.path.join(DOWNLOAD_BASE_PATH, filename)
    df = pd.read_excel(filepath, header=[0])
    df.columns = [
        'promotion_date',
        'promotion_bit',
        'clicks',
        'payments',
        'effects',
        'revenue']
    df['create_time'] = datetime.datetime.now()
    df['modify_time'] = datetime.datetime.now()
    df['promotion_date'] = pd.to_datetime(df['promotion_date'], errors='ignore')
    df[['clicks', 'payments']] = df[['clicks', 'payments']].astype(int, errors='ignore')

    df.to_sql(con=db.engine, name='taobao_product_effect', if_exists='append', index=False)
    print('import successful !')


def JD_import(filename):
    filepath = os.path.join(DOWNLOAD_BASE_PATH, filename)
    df = pd.read_excel(filepath, header=[0])
    df.columns = [
        'promotion_date',
        'promotion_bit',
        'clicks',
        'payments',
        'effects',
        'revenue']
    df['create_time'] = datetime.datetime.now()
    df['modify_time'] = datetime.datetime.now()
    df['promotion_date'] = pd.to_datetime(df['promotion_date'], errors='ignore')
    df[['clicks', 'payments']] = df[['clicks', 'payments']].astype(int, errors='ignore')

    df.to_sql(con=db.engine, name='taobao_product_effect', if_exists='append', index=False)
    print('import successful !')
