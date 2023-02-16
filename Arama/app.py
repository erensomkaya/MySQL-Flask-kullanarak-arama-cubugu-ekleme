@app.route("/search",methods = ["GET","POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        #buradaki keyword kısmı ise html'de yaratmamız geerekiyor.
        i = "Select * From makale where title like '%"+keyword+"%'"
        b = cursor.execute(i)
        if b == 0:
            flash("Aradığınız kelime bulunamadı.","warning")
            return redirect(url_for("makaleler"))
        else:
            #fetchall kullandık çünkü verilerin hepsini alıp kontrol etmesi gerekiyor.
            makaleler = cursor.fetchall()
            return render_template("makaleler.html",makaleler = makaleler)