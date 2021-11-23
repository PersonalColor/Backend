import express from 'express'
import tokenRouter from '../../lib/router/token'

const router = express.Router()

router.get('/', tokenRouter, async (req, res) => {})

router.post('/', tokenRouter, async (req, res) => {})

router.put('/', tokenRouter, async (req, res) => {})

router.delete('/', tokenRouter, async (req, res) => {})

export default router
