"""
This a a testing file to work on imports into dynamoDB

As a noSql database all I need is the thing I am storing
Type: (Category, Session, etc)   This will be
Recno: (serial number)
Data: (As Json)
"""

from util import *
import boto


class LookupItem:
    changed = False
    def __init__(self, tblname, hashKey, rangeKey, attrib = ""):
        tblname = tblname
        hashKey = hashKey
        rangeKey = rangeKey
        attrib = attrib
    def put_data(self, dbConn):
        tbl = dbConn.get_table(self.tblname)
        try:
            item = tbl.get_item(hashkey=self.hashKey,rangekey=self.rangekey)
            if changed:
                print 'update the record'
        else:
            item = tbl.new_item(
                hashkey=self.hashKey,
                rangekey=self.rangeKey,
                attrs=self.attrib
            )
        finally:
            item.put()
            







def createTbl(dbConnect, tblname, hashKey, rangeKey):
    table_schema = dbConnect.create_schema(
        hash_key_name=hashKey,
        hash_key_proto_value=str,
        range_key_name=rangeKey,
        range_key_proto_value=str
    )
    table = dbConnect.create_table(
        name=tblname,
        schema=table_schema,
        read_units=1,
        write_units=1
    )
    return table



def listTbl(dbConnect):
    # print list of tables from
    currentTbl = dbConnect.list_tables()  # get list of tables.

    for table in currentTbl:
        print "Table Name: ", table



def run():
    awsCred = loadCred('./awscred.json')  #get credentials
    dbConn = boto.connect_dynamodb(awsCred['access'], awsCred['secret'])  #connect to database
    listTbl(dbConn)
    #print "Creating Table..."
    #tbl = createTbl(dbConn,'Lookups','Type', 'Entry')
    tbl = dbConn.get_table('Lookups')
    print "Connected to table.."
    # test record build
    item_data = {
        'Priority': '1',
        'Description': 'Working on Rudimental items.',
        }

    item = tbl.new_item(
        # Our hash key is 'forum'
        hash_key='Categories',
        # Our range key is 'subject'
        range_key='Rudiments',
        # This has the
        attrs=item_data
    )
    print item
    print "Saving item to table.."
    item.put()
    print "getting item..."
    item = tbl.get_item(
        # Your hash key was 'forum_name'
        hash_key='Categories',
        # Your range key was 'subject'
        range_key='Rudiments'
    )
    print "Here is the record."
    print item

if __name__ == "__main__":
    run()
