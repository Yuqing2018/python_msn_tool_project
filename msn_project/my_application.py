from flask import Flask, request, url_for, redirect, render_template
from flask.views import MethodView
from msn_project.utility import excel_process
from msn_project.utility import db_models

app = Flask(__name__)
app.config.from_pyfile('config.py')

from jinja2 import PackageLoader, Environment

env = Environment(loader=PackageLoader('msn_project', 'templates'))  # 创建一个包加载器对象


class TaobaoDetailsListView(MethodView):  # 获取淘宝效果报表信息
    def get(self, page=1):
        result = db_models.Taobao_detail.query.paginate(page, per_page=30)
        return render_template('taobao_details.html', result=result)


@app.route('/')
def home():
    # template = env.get_template('layout.html')  # 获取一个模板文件
    # return template.render()  # 渲染
    return render_template("home.html")


@app.route('/taobao/')
def show_all_taobao():
    result = db_models.Taobao_detail.query.order_by(db_models.Taobao_detail.create_time.desc()).all()
    return render_template("taobao_details.html", result=result)


@app.route('/duomai/')
def show_all_duomai():
    result = db_models.Duomai_detail.query.order_by(db_models.Duomai_detail.create_time.desc()).all()
    return render_template('duomai_details.html', result=result)


@app.route('/duomai/upload', methods=['POST'])
def upload():
    # 判断文件是否合法
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in set(['xls', 'xlsx', 'csv'])

    f = request.files['duomai_file']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = f.filename
        print(fname)
        excel_process.duomai_import(fname)
    return redirect(url_for('show_all_duomai'))


@app.route('/taobao/upload', methods=['POST'])
def upload_taobao():
    # 判断文件是否合法
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in set(['xls', 'xlsx', 'csv'])

    f = request.files['taobao_file']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = f.filename
        print(fname)
        excel_process.taobao_import(fname)
    return redirect(url_for('show_all_taobao'))


@app.route('/jd/')
def show_all_jd():
    template = env.get_template('jd_detail.html')  # 获取一个模板文件
    return template.render()  # 渲染
    # return render_template("jd_detail.html")


if __name__ == '__main__':
    db_models.db.init_app(app)
    db_models.db.create_all()
    app.run()
