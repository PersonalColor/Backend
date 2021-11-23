import express from 'express'
import user from './user'
import healthCheck from './healthCheck'
import login from './login'
import logout from './logout'

const router = express.Router()

router.use('/user', user)
router.use('/login', login)
router.use('/logout', logout)
router.use('/', healthCheck)

export default router
