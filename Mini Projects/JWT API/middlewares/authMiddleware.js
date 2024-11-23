import jwt from 'jsonwebtoken';

export const authenticateToken = (req, res, next) => {
    const token = req.header('Authorization')?.split(' ')[1]
    if (!token){res.status(401).json({'message': 'Give token bro!'})}

    jwt.verify( token, process.env.jwt_secret, (err, user) => {
        if(err){res.status(401).json({'message': 'Give token bro!'})}
        req.user = user
        next()
    })
}