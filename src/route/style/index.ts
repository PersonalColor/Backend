import express from 'express'
import style from './style'

const router = express.Router()

router.use('/', style)

export default router
