import express from 'express'
import DataProductManager from '../../module/data/product/productManager'

const router = express.Router()

router.get('/', async (req, res) => {
  return res.json(DataProductManager.getProductList())
})

export default router
