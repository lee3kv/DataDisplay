import {MongoClient} from 'mongodb'

export const getBmeData = (req, res) => {
    // const today = new Date();
    // var date = today.getMonth()+1 + "_" + today.getDate()
    const client = new MongoClient("mongodb+srv://Senior:Senior2022@cluster0.o1ezz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
    try {
        client.connect(err => {
            if (err) throw err;
            client.db('Data').collection('BME').find({_id:{$exists: true}}).toArray((err, result) => {
                if (err) throw err;
                res.status(200).json(result[0]);
            })
        })
    } catch (err) {
        res.status(404).json('message: err.message')
    }
}

// export const getGpsData = (req, res) => {
//     const today = new Date();
//     var date = today.getMonth()+1 + "_" + today.getDate()
//     const client = new MongoClient("mongodb+srv://Senior:Senior2022@cluster0.o1ezz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
//     try {
//         client.connect(err => {
//             if (err) throw err;
//             client.db('Data').collection('BME').find({_id:{$exists: true}}).toArray((err, result) => {
//                 if (err) throw err;
//                 res.status(200).json(result[0]);
//             })
//         })
//     } catch (err) {
//         res.status(404).json('message: err.message')
//     }
// }