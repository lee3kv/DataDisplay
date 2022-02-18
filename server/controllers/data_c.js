import {get_mongo_c} from "../util/mongo_u"

export const get_posts = async (req, res) => {
    try {
        const latest_bme_data = await data_a.find();

        res.status(200).json(latest_bme_data)
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}