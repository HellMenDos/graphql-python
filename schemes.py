from ariadne import gql, QueryType, MutationType

query = QueryType()
mutation = MutationType()

type_defs = gql(
   """
   type User {
       id: Int!
       name: String!
       email: String!
       password: String!
    }  


   type Post {
       id: Int!
       user_id: Int!
       title: String!
       description: String!
    }  

   type Query {
       users: [User]
       posts: [Post]
       post(id: Int!): Post 
       post_by_user(user_id: Int!): [Post] 
   }

   type Mutation{
      login(email: String!, password: String!): User
      reg(email: String!, name: String!, password: String!): User
      create_post(user_id: Int!, title: String!, description: String!): Post
    }
   """
)