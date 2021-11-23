import express from 'express'
import mypage from './mypage'

const router = express.Router()

router.use('/', mypage)

export default router
