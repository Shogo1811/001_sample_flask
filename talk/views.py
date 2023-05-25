@app.route('/talk', method = 'POST')
def create_talk():
    log = Log(
        name=request.form.get('name')
        article=request.form.get('article')
    )

    try:
        db.session.add(log)
        db.session.commit()
    except:
        flash('入力した内容を確認してください（文字数・入力漏れなど）')
