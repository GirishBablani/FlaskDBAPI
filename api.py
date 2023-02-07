from flask import Flask,jsonify,request
import psycopg2
app = Flask(__name__)          

#Basic CRUD in postgresql @girishbablani546@gmail.com
@app.route('/tourist/data',methods = ['POST'])
def home():
    if request.method=="POST":
        try:
            conn = psycopg2.connect(         ##connection to the postgre server
            host="kandula.db.elephantsql.com",
            database="jfhlybsv",
            user="jfhlybsv",
            password="giQZwzp0CyO_QtWUsoMmVTgoBzR1Z6UO")
            records=[]
            cur = conn.cursor()
            cur.execute('SELECT * FROM tourist_places;')
            rows = cur.fetchall()
            for i in rows:
                records.append({"location_id":i[0],"title":i[1],"image":i[2],"visiting_hours":i[3],"tips":i[4],"built_by":i[5],"built_in":i[6],"destination_url":i[7]})     
            cur.close()
            conn.close()
            return jsonify({"status":True,"records":records})
        except Exception as e:
            return jsonify({"status":False,"exception":e}) 
@app.route("/tourist/post",methods=['POST','PUT','DELETE'])
def up_del_ins():
    if request.method=="POST":
        json_insert = request.json
        record = (json_insert["location_id"],json_insert["title"],json_insert["image"],json_insert["visiting_hours"],json_insert["tips"],json_insert["built_by"],json_insert["built_in"],json_insert["destination_url"])
        try:
            conn = psycopg2.connect(         ##connection to the postgre server
            host="kandula.db.elephantsql.com",
            database="jfhlybsv",
            user="jfhlybsv",
            password="giQZwzp0CyO_QtWUsoMmVTgoBzR1Z6UO")
            cur = conn.cursor()
            cur.execute("Insert into tourist_places values (%s,%s,%s,%s,%s,%s,%s,%s)",record)
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"status":True,"message":"The record is inserted successfully"})
            
        except Exception as e:
            return jsonify({"status":False,"exception":e})   
    if request.method == "PUT":
        json_update = request.json
        update_record = (json_update["value1"],json_update["title"])
        try:
            conn = psycopg2.connect(         ##connection to the postgre server
            host="kandula.db.elephantsql.com",
            database="jfhlybsv",
            user="jfhlybsv",
            password="giQZwzp0CyO_QtWUsoMmVTgoBzR1Z6UO")
            cur = conn.cursor()
            query = f"update tourist_places set {json_update['field1']}"
            cur.execute(query+"=%s where title=%s",update_record)
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"status":True,"message":"Your record is updated successfully"})
        except Exception as e:
            return jsonify({"status":False,"exception":e})
    if request.method=="DELETE":
        delete_json = request.json
        try:
            conn = psycopg2.connect(         ##connection to the postgre server
            host="kandula.db.elephantsql.com",
            database="jfhlybsv",
            user="jfhlybsv",
            password="giQZwzp0CyO_QtWUsoMmVTgoBzR1Z6UO")
            cur = conn.cursor()
            cur.execute(f"Delete from tourist_places where title='{delete_json['title']}'")
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"status":True,"message":"The record is successfully deleted"})
        except Exception as e:
            return jsonify({"status":False,"exception":e})   

##This is for searching in get @girishbablani546@gmail.com
@app.route("/tourist/search",methods=['POST'])
def search():
    title = request.args.get("title")
    try:
        conn = psycopg2.connect(         ##connection to the postgre server
        host="kandula.db.elephantsql.com",
            database="jfhlybsv",
            user="jfhlybsv",
            password="giQZwzp0CyO_QtWUsoMmVTgoBzR1Z6UO")
        search_data = []
        cur = conn.cursor()
        cur.execute(f"Select * from tourist_places where title='{title}'")
        for i in cur.fetchall():
            search_data.append({"location_id":i[0],"title":i[1],"image":i[2],"visiting_hours":i[3],"tips":i[4],"built_by":i[5],"built_in":i[6],"destination_url":i[7]})
        cur.close()
        conn.close()
        return jsonify({"status":True,"records":search_data})
    except Exception as e:
        return({"status":False,"exception":e})   


if __name__=="__main__":   
    app.run(debug=False)    