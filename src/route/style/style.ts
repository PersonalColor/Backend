import express from 'express'
import DataStyleManager from '../../module/data/style/styleManager'

const router = express.Router()

router.get('/', async (req, res) => {
  return res.json(DataStyleManager.getStyleList())
})

export default router
