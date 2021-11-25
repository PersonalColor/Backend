import express from 'express'
import user from './user'
import healthCheck from './healthCheck'
import login from './login'
import logout from './logout'
import product from './product'
import style from './style'
import diagnosis from './diagnosis'
import data from './data'

const router = express.Router()

router.use('/user', user)
router.use('/login', login)
router.use('/logout', logout)
router.use('/product', product)
router.use('/style', style)
router.use('/', healthCheck)
router.use('/diagnosis', diagnosis)
router.use('/data', data)

export default router
