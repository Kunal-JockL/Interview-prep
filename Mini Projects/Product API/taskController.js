import product from "./productModel.js";

export const productsUpload = async (req, res) => {
    try{
        const products = req.body;
        const productsUploaded = await product.insertMany(products.products);
        console.log(productsUploaded)
        res.status(201).json(productsUploaded)
    }catch(error){
        console.log(error.message);
        res.status(401).json(error.message)
    }
} 

export const getProducts = async (req, res) => {
    try{
        let { page, limit, category, sortBy, order} = req.query
        limit = parseInt(limit)
        page = parseInt(page)

        const filteredProducts = await product.find({category: category})
        
        const sortedProducts = filteredProducts.sort((a,b) => 
            {
                if(order === 'desc'){
                    return a[sortBy].localeCompare(b[sortBy]) 
                }else{
                    return b[sortBy].localeCompare(a[sortBy]) 
                }
            }
        )   

        let dividedArray = null
        
        try{
            dividedArray = sortedProducts.slice(limit*(page-1),limit*(page))
        }catch(error){
            dividedArray = sortedProducts.slice(limit*(page-1),sortedProducts.length)
        }

        //console.log(dividedArray)
        
        //console.log(page, limit, category, sortBy, order)
        res.status(201).json({"products": dividedArray, "pagination": { 
            "currentPage": page,
            "totalPages": Math.ceil(sortedProducts.length/limit),
            "totalCount": sortedProducts.length
        }})

    }catch(error){
        console.log(error.message);
        res.status(401).json(error.message)
    }
}